import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

frequence = 16000
paquets = []
en_pause = False

def callback(indata, frames, time, status):
    if not en_pause:
        paquets.append(indata.copy())

print("Enregistrement en cours.")
print("[Entrée] = pause/reprise  |  tape 'stop' puis [Entrée] = terminer")

stream = sd.InputStream(samplerate=frequence, channels=1, callback=callback)
stream.start()

while True:
    commande = input()
    if commande.strip().lower() == "stop":
        break
    else:
        en_pause = not en_pause
        if en_pause:
            print("Pause")
        else:
            print("Reprise")

stream.stop()
stream.close()
print("Enregistrement terminé.")

enregistrement = np.concatenate(paquets, axis=0)
write("test.wav", frequence, enregistrement)
print("Sauvegardé dans test.wav")