## Installation
### pip
```bash
python -m venv env

# pip install nbdime
# nbdime config-git --enable --global

pip install tensorflow==2.0.0
```

### Docker
```bash
docker build -t ukulele_chords_detector .
docker run -v $(pwd):/app -it --rm ukulele_chords_detector python main.py
docker run -v $(pwd):/app -it --rm -p 8888:8888 ukulele_chords_detector
```

## Collecting data

```bash
# record audio
# https://superuser.com/questions/889912/how-to-record-10-seconds-of-audio-with-sox
# man sox | grep -A 15 "\-b BITS"
# man sox | grep -A 20 "\-r, --rate"
sox -b 32 -e unsigned-integer -r 96k -c 2 -d --clobber --buffer $((96000*2*10)) ./chords.wav trim 0 10
sox -b 32 -e unsigned-integer -r 96k -c 2 -d --clobber ./chords.wav trim 0 20

# denoise it
# https://stackoverflow.com/questions/44159621/how-to-denoise-audio-with-sox
sox chords.wav noise-audio.wav trim 0 0.300
sox noise-audio.wav -n noiseprof noise.prof
sox chords.wav audio-clean.wav noisered noise.prof 0.21

# split it
# https://stackoverflow.com/questions/5210582/sox-fails-to-split-files
sox -V3 audio-clean.wav splitted_chord.wav silence 1 0.1 0.1% 1 0.1 0.1% : newfile : restart

# remove insignificant files
# https://gist.github.com/devoncrouse/5534261
# https://explainshell.com/explain?cmd=find+.+-type+f+-name+%22*.mp3%22+-mmin+%2B30+-size+-500k+-delete
find . -type f -name '*.wav' -mmin -5 -size -2k -delete

# get text stats
# https://stackoverflow.com/questions/21756237/get-a-spectrum-of-frequencies-from-wav-riff-using-linux-command-line
sox chord.wav -n stat -freq >& chord.csv
sed -i 's/.*\s//' chord.csv
printf '%s\n%s\n' "frequency" "$(cat chord.csv)" > chord.csv
```


