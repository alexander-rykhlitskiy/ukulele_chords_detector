import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('chords.txt')
# df = pd.DataFrame(df['frequency'], index=df['time'])
# df.plot()
# plt.show()

from scipy.io import wavfile
import os

here_path = os.path.dirname(os.path.realpath(__file__))
wav_file_name = 'samples/chords.wav'
wave_file_path = os.path.join(here_path, wav_file_name)
sr, signal = wavfile.read(wave_file_path)

y = signal[:, 0]  # use the first channel (or take their average, alternatively)
t = np.arange(len(y)) / float(sr)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y')

plt.show()
