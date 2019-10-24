# Ukulele Chords Detector
The goal was to teach neural network to detect chord played on ukulele. Network was trained and tested on single notes, but any other short sound (chord, bang, knock) can be categorized too. The only thing needed for that is `wav` files of these sounds.

Recorded sound samples are located in `samples` directory. Each directory corresponds to some kind of sound. Each sound directory contains directories for training and for testing trained network. New samples can be collected using steps at the bottom of the file.

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

### Record and split the sound
```bash
./record.sh 30
```
 After running this script, start playing one note (sound) many times in a row with some interval (1 second is enough) for 30 seconds in this case. Output is as many files as you pulled the string (made any sound). Please check that each file has exactly one sample of sound with `play splitted_chord001.wav` (or any other player), remove incorrect files and move correct ones into `samples` directory.

 New sounds can be added in `samples` directory in path like
 ```bash
 samples/{sound name, e.g. A or C or E note, Dm chord, bang}/{train or test}/{anything (e.g. number of recording)}/*.wav
 ```

## Development
[jupytext](https://github.com/mwouts/jupytext) is used, so both python command with `main.py` and jupyter with `main.ipynb` can run the program. After changing one of these files please don't forget to update another running jupyter.
