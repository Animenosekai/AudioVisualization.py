# AudioVisualization.py
 A set of audio analysis and visualisation tool

### Dependencies

AudioVisualization depends on several modules which requires an installation through pip (Python Package Manager)

Including:
- Numpy
- Matplotlib
- Aubio
- Pyaudio


### Explanation for each file

- wave_viualizer.py

This script just shows the audiowaves of your microphone input in realtime.

- wavelength_to_rgb.py

A script which converts wavelength to an RGB color. *(Thanks to Noah.org for this script, http://www.noah.org/wiki/Wavelength_to_RGB_in_Python)*

> Also available on my LifeEasy python library (coming soon)

- realtime_analyze.py

Gives you the volume and the pitch (in Hz) printed in real-time (in your python console).

- pitch_color_visualizer.py

Displays a color representing the current average frequency playing from your default microphone input.

The color range is as follows: **Red** *(low frequency)* to **Blue** *(high frequency)* (you can inverted that in the script doing simple maths).

- pitch_plotting.py

Plots the current average frequency playing from your default microphone input and gives an average from the beggining of the session.


### Test Data

The test data folder currently contains two files (I had more but not needed here) to test the programs (these files are just raw piano sounds playing 3 notes at two different octaves).

What I did to test the programs is going to tone generator websites too (*Like this one: https://www.szynalski.com/tone-generator/*). 

> ©Anime no Sekai - 2020
