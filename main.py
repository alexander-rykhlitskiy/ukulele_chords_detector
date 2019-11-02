# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
import os

SHIFT_START = 2000
CAPTURE     = 5000

# https://stackoverflow.com/questions/53308674/audio-frequencies-in-python
def read_wav(wav_file_name):
    sr, signal = wavfile.read(wav_file_name)
    return (sr, signal[SHIFT_START:(SHIFT_START + CAPTURE), 0]) # use the first channel (or take their average, alternatively)

def fetch_frequencies(wav_file_name):
    sr, y = read_wav(wav_file_name)
    return y

def show_file_spectrum(wav_file_name):
    sr, y = read_wav(wav_file_name)
    show_array_spectrum(y, sr)

def show_array_spectrum(y, sample_rate=1, normalize_y_axe=True):
    t = np.arange(len(y)) / float(sample_rate)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(t, y)
    plt.xlabel('t')
    plt.ylabel('y')
    axes = plt.gca()
    if normalize_y_axe:
        axes.set_ylim([-1e9, 1e9])

    plt.show()

# %%
SAMPLES_DIR = 'samples'
TRAIN_DIR = 'train'
TEST_DIR = 'test'

show_file_spectrum(os.path.join(SAMPLES_DIR, 'A', TRAIN_DIR, '1_out_of_tune', 'splitted_chord009.wav'))

# %%
show_file_spectrum(os.path.join(SAMPLES_DIR, 'C', TRAIN_DIR, '1', 'splitted_chord007.wav'))

# %%
show_file_spectrum(os.path.join(SAMPLES_DIR, 'E', TRAIN_DIR, '1', 'splitted_chord007.wav'))

# %%
import glob
import itertools

sound_names_index = {sound_name: idx for idx, sound_name in enumerate(os.listdir(SAMPLES_DIR))}
sound_names_index_reverted = {v: k for k, v in sound_names_index.items()}
print('Following sounds are going to be categorized')
print(list(sound_names_index.keys()))

# %%
def parse_sound_name(path):
    sound_folders_depth = 1
    return os.path.normpath(path).split(os.path.sep)[sound_folders_depth]

def list_files(directory):
    files = glob.glob(os.path.join(SAMPLES_DIR, '*', directory, '*', '*.wav'))
    return {file: sound_names_index[parse_sound_name(file)] for file in files}

train_files = list_files(TRAIN_DIR)
test_files  = list_files(TEST_DIR)

# %%
import datetime
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

def rescale(tensor1, tensor2):
    max_value = tf.reduce_max([tf.reduce_max(tensor1), tf.reduce_max(tensor2)])
    min_value = tf.reduce_min([tf.reduce_min(tensor1), tf.reduce_min(tensor2)])
    result1 = tf.truediv(tf.subtract(tensor1, min_value), tf.subtract(max_value, min_value))
    result2 = tf.truediv(tf.subtract(tensor2, min_value), tf.subtract(max_value, min_value))
    return result1 - 0.5, result2 - 0.5 # positive numbers should be interchanged with negative ones

def files_to_tensors(files):
    return tf.convert_to_tensor([tf.convert_to_tensor(fetch_frequencies(file), np.float64) for file in files])

def labeled_files_to_tensors(labeled_files):
    x = files_to_tensors(labeled_files.keys())
    y = tf.convert_to_tensor(list(labeled_files.values()))
    return x, y

x, y           = labeled_files_to_tensors(train_files)
x_test, y_test = labeled_files_to_tensors(test_files)
x, x_test = rescale(x, x_test)
show_array_spectrum(x[0], normalize_y_axe=False)

# %%
def create_model():
    model = keras.Sequential([
        keras.layers.Dense(CAPTURE),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(3, activation='softmax')
    ])
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
    return model

def tensorboard_callback():
    log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    return tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

model = create_model()
model.fit(x, y, validation_data=(x_test, y_test), callbacks=[tensorboard_callback()], epochs=15)

# %%
# became kind of legacy after introducing validation_data param.
# But still used to get predictions for specific files.

def predict_files(files):
    files_data = files_to_tensors(files)
    for idx, prediction in enumerate(model.predict(files_data)):
        sound_name = sound_names_index_reverted[list(prediction).index(1)]
        print(f'{sound_name} - {files[idx]}')

predict_files(list(test_files.keys()))

# %%
%load_ext tensorboard
%tensorboard --logdir logs/fit
