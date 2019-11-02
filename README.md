# Ukulele Chords Detector
The goal was to teach neural network to detect chord played on ukulele. Network was trained and tested on single notes, but any other short sound (chord, bang, knock) can be categorized too. The only thing needed for that is `wav` files of these sounds.

Recorded sound samples are located in `samples` directory. Each directory corresponds to some kind of sound. Each sound directory contains directories for training and for testing trained network. New samples can be collected using steps at the bottom of the file.

*For implementation of this task using Uber's Ludwig toolbox see https://github.com/alexander-rykhlitskiy/ukulele_chords_detector_ludwig*

## Installation and running
### Binder
Just click

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/alexander-rykhlitskiy/ukulele_chords_detector/master)

Open `main.ipynb` and click `Cell -> Run all`

### Docker
```bash
docker build -t ukulele_chords_detector .

docker run -v $PWD:/app -it --rm -p 8888:8888 ukulele_chords_detector python main.py
# or to run jupyter lab
docker run -v $PWD:/app -it --rm -p 8888:8888 ukulele_chords_detector
```

### venv
First install python 3.7. Then
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt

python main.py
# or to run jupyter lab
jupyter lab
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

## TODO
* Create confusion matrix https://www.tensorflow.org/tensorboard/image_summaries#building_an_image_classifier
* Rescale values to (0..1)

## Development
[jupytext](https://github.com/mwouts/jupytext) is used, so both python command with `main.py` and jupyter with `main.ipynb` can run the program. After changing one of these files please don't forget to update another running jupyter.
