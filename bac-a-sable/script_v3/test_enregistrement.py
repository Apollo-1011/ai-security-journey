import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

frequence = 16000

# La liste qui va accumuler les paquets d'audio (le récipient sous le robinet)
paquets = []

# Le callback : sounddevice l'appelle automatiquement à chaque paquet reçu
def callback(indata, frames, time, status):
    paquets.append(indata.copy())

# On ouvre le stream en lui donnant notre callback
print("Enregistrement... Appuie sur Entrée pour arrêter.")
stream = sd.InputStream(samplerate=frequence, channels=1, callback=callback)
stream.start()

# Le code principal attend l'appui sur Entrée (le stream tourne en fond pendant ce temps)
input()

# On ferme le stream → le callback s'arrête
stream.stop()
stream.close()
print("Enregistrement terminé.")

# On assemble tous les paquets en un seul audio
enregistrement = np.concatenate(paquets, axis=0)

# On sauvegarde
write("test.wav", frequence, enregistrement)
print("Sauvegardé dans test.wav")