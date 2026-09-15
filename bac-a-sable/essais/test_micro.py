import sounddevice as sd
from scipy.io.wavfile import write

frequence = 16000
duree = 5

print("Go!")
enregistrement = sd.rec(int(duree * frequence), samplerate=frequence, channels=1)
sd.wait()
print("Fini !")

write("test.wav", frequence, enregistrement)