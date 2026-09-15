import sounddevice as sd
from scipy.io.wavfile import write
import whisper

frequence = 16000
duree = 5

print("Parle maintenant...")
enregistrement = sd.rec(int(duree * frequence), samplerate=frequence, channels=1)
sd.wait()
print("Fini !")

write("test.wav", frequence, enregistrement)

print("Chargement du modèle...")
model = whisper.load_model("base", device="cuda")

print("Transcription en cours...")
resultat = model.transcribe("test.wav")

print("Texte transcrit :")
print(resultat["text"])

with open("test.txt", "a", encoding="utf-8") as f:
    f.write(resultat["text"] + "\n")

print("Texte ajouté au fichier test.txt")