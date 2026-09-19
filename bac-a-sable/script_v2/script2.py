import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import ollama
import subprocess
from pathlib import Path

# Dossier où se trouve CE script, peu importe d'où on le lance
DOSSIER_SCRIPT = Path(__file__).resolve().parent
chemin_wav = DOSSIER_SCRIPT / "test.wav"
chemin_md = DOSSIER_SCRIPT / "compte-rendu.md"

# --- Consigne pour Ollama (les règles, constantes) ---
CONSIGNE = """Ton objectif : m'aider à transformer un texte brut en un texte en markdown. Voici les consignes à respecter. Il faut que tu restes fidèle au texte que je te donne. Tu ne dois jamais ajouter du texte que je n'aurais pas dit. tu ne dois jamais implémenter une idée que je n'aurais pas formulée. la modification que tu dois faire, c'est la correction des fautes d'orthographe et ajouter de la ponctuation. Pour le titre en markdown, tu dois utiliser le caractère # ou ## pour mettre en valeur les titres et sous titres, interdiction d'utiliser ===== pour les titres. tu dois utiliser des listes. Seulement pour des vraies énumérations. Pas à chaque fois. Seulement quand c'est pertinent. Dernière règle, tu ne dois rien ajouter autour de ta réponse. Donne-moi uniquement le texte reformulé en markdown."""

# --- Paramètres ---
frequence = 16000
duree = 15

# --- Maillon 1a : capter la voix ---
print("Go!")
enregistrement = sd.rec(int(duree * frequence), samplerate=frequence, channels=1)
sd.wait()
print("Fini !")

write(chemin_wav, frequence, enregistrement)

# --- Maillon 1b : transcrire (Whisper, brut) ---
print("Chargement du modèle Whisper...")
model = whisper.load_model("base", device="cuda")

print("Transcription en cours...")
resultat = model.transcribe(str(chemin_wav))
print("Transcription brute :")
print(resultat["text"])

# --- Maillon 1c : reformater en markdown (Ollama) ---
print("Reformatage en markdown...")
reponse = ollama.chat(
    model="llama3.1:8b",
    messages=[
        {"role": "system", "content": CONSIGNE},
        {"role": "user", "content": resultat["text"]}
    ]
)
texte_markdown = reponse["message"]["content"]
print("Markdown généré :")
print(texte_markdown)

# --- Maillon 2 : écrire le markdown dans le fichier ---
with open(chemin_md, "a", encoding="utf-8") as f:
    f.write(texte_markdown + "\n")
print("Markdown ajouté à compte-rendu.md")

# --- Maillon 3 : pousser sur GitHub ---
subprocess.run(["git", "add", "compte-rendu.md"], cwd=DOSSIER_SCRIPT)
subprocess.run(["git", "add", "compte-rendu.md"], cwd=DOSSIER_SCRIPT)

resultat_commit = subprocess.run(["git", "commit", "-m", "Ajout d'un compte rendu"], cwd=DOSSIER_SCRIPT)

if resultat_commit.returncode == 0:
    resultat_push = subprocess.run(["git", "push"], cwd=DOSSIER_SCRIPT)
    if resultat_push.returncode == 0:
        print("Poussé sur GitHub !")
    else:
        print("Échec du push (problème réseau ou authentification ?).")
else:
    print("Rien de nouveau à sauvegarder.")