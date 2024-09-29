import matplotlib.pyplot as plt
import numpy as np

N = 10000

sawtooth = np.empty(N)
for i in range(N):
    sawtooth[i] = 9 - i % 10

fft = np.fft.fft(sawtooth)

# plt.plot(fft.real)
# plt.plot(fft.imag)

# ifft = np.fft.ifft(fft)
# plt.plot(ifft.real)

plt.plot(fft.real)
plt.plot(fft.imag)

plt.show()
