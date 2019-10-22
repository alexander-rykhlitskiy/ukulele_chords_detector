#!/bin/bash

# record and trim
# https://superuser.com/questions/889912/how-to-record-10-seconds-of-audio-with-sox
# man sox | grep -A 15 "\-b BITS"
# man sox | grep -A 20 "\-r, --rate"
sox -b 32 -e unsigned-integer -r 96k -c 2 -d --clobber ./chords.wav trim 0 10

# denoise
# https://stackoverflow.com/questions/44159621/how-to-denoise-audio-with-sox
sox chords.wav noise-audio.wav trim 0 0.300
sox noise-audio.wav -n noiseprof noise.prof
sox chords.wav audio-clean.wav noisered noise.prof 0.21

# split
# https://stackoverflow.com/questions/5210582/sox-fails-to-split-files
sox -V3 audio-clean.wav splitted_chord.wav silence 1 0.1 0.1% 1 0.1 0.1% : newfile : restart

# remove insignificant files
# https://gist.github.com/devoncrouse/5534261
# https://explainshell.com/explain?cmd=find+.+-type+f+-name+%22*.mp3%22+-mmin+%2B30+-size+-500k+-delete
find . -type f -name '*.wav' -mmin -5 -size -200k -delete

rm audio-clean.wav chords.wav noise-audio.wav noise.prof
