# Ukulele Chord Detector

## Installation
### pip
```bash
python -m venv env
source env/bin/activate
pip install tensorflow==2.0.0 jupytext==1.2.4 scipy matplotlib numpy
python main.py

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


