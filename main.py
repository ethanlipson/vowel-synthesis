import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np

a = wavfile.read("test.wav")
data = np.array(a[1], dtype="float")[:, 0]

# plt.plot(data[100000:101000])
# plt.show()

# perform fft and plot

fft = np.fft.fft(data)
fft[20000:] = 0
# plt.plot(np.abs(fft))
# plt.show()
high_pass = np.fft.ifft(fft)

# save

# wavfile.write("high_pass.wav", a[0], high_pass.astype("int16"))

plt.plot(data[100000:101000])
plt.show()
