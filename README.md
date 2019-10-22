# Ukulele Chord Detector

## Installation
### pip
```bash
python -m venv env
# INSTALL pip modules from Dockerfile

# pip install nbdime
# nbdime config-git --enable --global
```

### Docker
```bash
docker build -t ukulele_chords_detector .
docker run -v $(pwd):/app -it --rm -p 8888:8888 ukulele_chords_detector
```

## Collecting data

### Record and split note or chord
```bash
./record_chord.sh
```


