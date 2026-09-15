import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import subprocess
from pathlib import Path

# Dossier où se trouve CE script, peu importe d'où on le lance
DOSSIER_SCRIPT = Path(__file__).resolve().parent
chemin_wav = DOSSIER_SCRIPT / "test.wav"
chemin_preuve = DOSSIER_SCRIPT / "preuve.txt"

# --- Paramètres ---
frequence = 16000
duree = 5

# --- Maillon 1a : capter la voix ---
print("Go!")
enregistrement = sd.rec(int(duree * frequence), samplerate=frequence, channels=1)
sd.wait()
print("Fini !")

write(chemin_wav, frequence, enregistrement)

# --- Maillon 1b : transcrire ---
print("Chargement du modèle...")
model = whisper.load_model("base", device="cuda")

print("Transcription en cours...")
resultat = model.transcribe(str(chemin_wav))
print("Texte transcrit :")
print(resultat["text"])

# --- Maillon 2 : écrire dans le fichier ---
with open(chemin_preuve, "a", encoding="utf-8") as f:
    f.write(resultat["text"] + "\n")
print("Texte ajouté à preuve.txt")

# --- Maillon 3 : pousser sur GitHub ---
subprocess.run(["git", "add", "preuve.txt"], cwd=DOSSIER_SCRIPT)
subprocess.run(["git", "commit", "-m", "Ajout d'une transcription"], cwd=DOSSIER_SCRIPT)
subprocess.run(["git", "push"], cwd=DOSSIER_SCRIPT)
print("Poussé sur GitHub !")