# Ukulele Chord Detector

## Installation
### pip
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
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


