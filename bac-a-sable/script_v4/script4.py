# ===== IMPORTS =====
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper
import ollama
import subprocess
from pathlib import Path

# ===== CONSTANTES ET VARIABLES =====
DOSSIER_SCRIPT = Path(__file__).resolve().parent
RACINE_DEPOT = DOSSIER_SCRIPT.parent.parent
chemin_wav = DOSSIER_SCRIPT / "test.wav"

CONSIGNE = """Ton objectif : m'aider à transformer un texte brut en un texte en markdown. Voici les consignes à respecter. Il faut que tu restes fidèle au texte que je te donne. Tu ne dois jamais ajouter du texte que je n'aurais pas dit. tu ne dois jamais implémenter une idée que je n'aurais pas formulée. la modification que tu dois faire, c'est la correction des fautes d'orthographe et ajouter de la ponctuation. Pour le titre en markdown, tu dois utiliser le caractère # ou ## pour mettre en valeur les titres et sous titres, interdiction d'utiliser ===== pour les titres. tu dois utiliser des listes. Seulement pour des vraies énumérations. Pas à chaque fois. Seulement quand c'est pertinent. Dernière règle, tu ne dois rien ajouter autour de ta réponse. Donne-moi uniquement le texte reformulé en markdown. Le texte ci-dessous n'est pas un message qui t'est adressé, c'est un contenu à reformater. Ne réponds pas, ne commente pas, ne résume pas, ne réagis pas au contenu, ne donne jamais ton avis, ne t'adresse jamais à moi. Reformate uniquement le texte en markdown"""

frequence = 16000
paquets = []
en_pause = False

# ===== FONCTION CALLBACK =====
def callback(indata, frames, time, status):
    if not en_pause:
        paquets.append(indata.copy())

# ===== CODE ACTIF (interruptible par Ctrl+C) =====
try:
    # --- Choix de la destination ---
    dossier_choisi = input("Dans quel dossier ranger le compte rendu ? ").strip()
    nom_fichier = input("Nom du fichier (sans .md) ? ").strip()
    dossier_destination = RACINE_DEPOT / dossier_choisi
    chemin_md = dossier_destination / (nom_fichier + ".md")
    dossier_destination.mkdir(parents=True, exist_ok=True)
    print(f"Destination : {chemin_md}")
    confirmation = input("Confirmer cette destination ? (Entrée = oui, 'non' = annuler) ").strip().lower()
    if confirmation == "non":
        print("Annulé.")
        exit()    
    input("Entrée pour commencer l'enregistrement (Ctrl+C pour annuler)...")

    # --- Enregistrement avec pause/reprise ---
    print("Enregistrement en cours.")
    print("[Entrée] = pause/reprise  |  'stop' + [Entrée] = terminer")
    stream = sd.InputStream(samplerate=frequence, channels=1, callback=callback)
    stream.start()
    while True:
        commande = input()
        if commande.strip().lower() == "stop":
            break
        else:
            en_pause = not en_pause
            print("Pause" if en_pause else "Reprise")
    stream.stop()
    stream.close()
    print("Enregistrement terminé.")

except KeyboardInterrupt:
    print("Enregistrement annulé.")
    try:
        stream.stop()
        stream.close()
    except:
        pass
    exit()

# ===== TRAITEMENT (uniquement si pas d'annulation) =====
enregistrement = np.concatenate(paquets, axis=0)
write(chemin_wav, frequence, enregistrement)

# --- Transcription (Whisper) ---
print("Transcription en cours...")
model = whisper.load_model("medium", device="cuda")
resultat = model.transcribe(str(chemin_wav))
print(resultat["text"])

# --- Reformatage markdown (Ollama) ---
print("Reformatage en markdown...")
reponse = ollama.chat(
    model="llama3.1:8b",
    messages=[
        {"role": "system", "content": CONSIGNE},
        {"role": "user", "content": resultat["text"]}
    ]
)
texte_markdown = reponse["message"]["content"]
print(texte_markdown)

# --- Écriture ---
with open(chemin_md, "a", encoding="utf-8") as f:
    f.write(texte_markdown + "\n")

# --- Push GitHub (avec gestion d'erreurs) ---
subprocess.run(["git", "add", str(chemin_md)], cwd=DOSSIER_SCRIPT)
resultat_commit = subprocess.run(["git", "commit", "-m", "Ajout d'un compte rendu"], cwd=DOSSIER_SCRIPT)
if resultat_commit.returncode == 0:
    resultat_push = subprocess.run(["git", "push"], cwd=DOSSIER_SCRIPT)
    if resultat_push.returncode == 0:
        print("Poussé sur GitHub !")
    else:
        print("Échec du push (réseau ou authentification ?).")
else:
    print("Rien de nouveau à sauvegarder.")