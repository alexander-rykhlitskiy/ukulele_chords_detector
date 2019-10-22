# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
import os

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import glob

FREQUENCIES_COUNT = 50000
# https://stackoverflow.com/questions/25876640/subsampling-every-nth-entry-in-a-numpy-array
EACH_N_ELEMENT = 10

# https://stackoverflow.com/questions/53308674/audio-frequencies-in-python
def read_wav(wav_file_name):
    sr, signal = wavfile.read(wav_file_name)
    return (sr, signal[:FREQUENCIES_COUNT:EACH_N_ELEMENT, 0]) # use the first channel (or take their average, alternatively)

def fetch_frequencies(wav_file_name):
    sr, y = read_wav(wav_file_name)
    return y

def show_frequency_spectrum(wav_file_name):
    sr, y = read_wav(wav_file_name)
    t = np.arange(len(y)) / float(sr)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(t, y)
    plt.xlabel('t')
    plt.ylabel('y')
    axes = plt.gca()
    axes.set_ylim([-1e9,1e9])

    plt.show()
# -

show_frequency_spectrum('samples/A/train/1_out_of_tune/splitted_chord007.wav')

show_frequency_spectrum('samples/C/train/1/splitted_chord007.wav')

show_frequency_spectrum('samples/E/train/1/splitted_chord007.wav')

# +
def files_to_tensors(files):
    return tf.convert_to_tensor([tf.convert_to_tensor(fetch_frequencies(file), np.int32) for file in files])
# -

model = keras.Sequential([
    keras.layers.Dense(FREQUENCIES_COUNT),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(3, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# +
a_train_files = glob.glob("samples/A/train/*/*.wav")
c_train_files = glob.glob("samples/C/train/*/*.wav")
e_train_files = glob.glob("samples/E/train/*/*.wav")

train_files_data = files_to_tensors(a_train_files + c_train_files + e_train_files)
labels_values = {'A': 0, 'C': 1, 'E': 2}
labels_names = {v: k for k, v in labels_values.items()}
train_labels = tf.convert_to_tensor([labels_values['A']] * len(a_train_files) + [labels_values['C']] * len(c_train_files) + [labels_values['E']] * len(e_train_files), np.int32)
# -

model.fit(train_files_data, train_labels, epochs=5)


# +
def test_files(files):
    test_files_data = files_to_tensors(files)
    for idx, prediction in enumerate(model.predict(test_files_data)):
        print(f'{labels_names[list(prediction).index(1)]} - {files[idx]}')

a_test_files = glob.glob("samples/A/test/*/*.wav")
c_test_files = glob.glob("samples/C/test/*/*.wav")
e_test_files = glob.glob("samples/E/test/*/*.wav")

test_files(a_test_files + c_test_files + e_test_files)
# -

test_files(['samples/A/train/1_out_of_tune/splitted_chord009.wav'])


