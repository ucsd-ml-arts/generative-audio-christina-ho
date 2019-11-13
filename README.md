# Project 2 Generative Audio

Christina Ho, cgh003@ucsd.edu

## Abstract

Many people may know that since taking office, President Trump is not the most eloquent speaker. However, President Obama was. For this project, I train audios of President Obama speaking on a text-to-speech voice cloning algorithm so that it will create an audio that sounds like as if former President Barack Obama was speaking something President Trump has said. The algorithm uses both WaveRNN and TacoTron2 to use pretrained models and the wav file given it to generate a wav file that mimics the patterns of Obama's voice. 

## Model/Data

Briefly describe the files that are included with your repository:
- Pretrained models included from https://github.com/cgh003/Real-Time-Voice-Cloning
- Over an hour of Obama's voice: 

## Code

Your code for generating your project:
- Python: main.py - Include the file path to a piece of text to be spoken.

## Results

Documentation of your results in an appropriate format, both links to files and a brief description of their contents:
- `.wav` files or `.mp4`

## Technical Notes

Any implementation details or notes we need to repeat your work. 
- first add the submodule for voice cloning
- pip install -r requirements.txt
- Run download.sh

## Reference

References to any papers, techniques, repositories you used:
- https://github.com/CorentinJ/Real-Time-Voice-Cloning
