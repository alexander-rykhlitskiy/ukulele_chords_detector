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
./record_chord.sh
```


