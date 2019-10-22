# Ukulele Chords Detector
The goal is to teach Keras neural network to detect chord played on ukulele, but currently it can only detect notes.

Notes samples are in `samples` folder. Each folder corresponds to some note. Each note folder contains folders for training and for testing trained network. New samples can be collected using steps below.

## Installation and running
### venv
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

## Collecting data for training
Install [sox](http://sox.sourceforge.net/)

Mac
```bash
brew install sox
```

Ubuntu
```bash
sudo apt-get install sox
```

### Record and split note or chord
```bash
./record_chord.sh 30
```
 After running this script, start playing one note many times in a row with some interval (1 second is enough) for 30 seconds in this case. Output is as many files as you pulled the string. Please check that each file has exactly one note with `play splitted_chord001.wav` (or any other player), remove incorrect files and move correct ones into `samples` folder.

### TODO
* Detect notes for training by folders in `samples` folder
