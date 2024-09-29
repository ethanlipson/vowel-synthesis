from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

F1 = 116

rate, raw = wavfile.read("low-mid-unrounded.wav")
data = np.array(raw, dtype="float")[:, 0]

fft = np.fft.fft(data)

for i in range(fft.shape[0]):
    nearest = round(i / F1) * F1
    if abs(i - nearest) > 10:
        fft[i] = 0

ifft = np.fft.ifft(fft) * 10

plt.plot(fft[:5000])
plt.show()

wavfile.write("f1.wav", rate, ifft.real.astype("int16"))
