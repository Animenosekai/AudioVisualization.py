print('Loading...')

import numpy as np
import matplotlib.pyplot as plt
import aubio
import numpy as num
import pyaudio
import wave
import os

def wavelength_to_rgb(wavelength, gamma=0.8):

    '''This converts a given wavelength of light to an
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''

    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return [int(R), int(G), int(B)]

# PyAudio object.
p = pyaudio.PyAudio()

# Open stream.
stream = p.open(format=pyaudio.paFloat32,
    channels=1, rate=44100, input=True,
    frames_per_buffer=1024)

# Aubio's pitch detection.
pDetection = aubio.pitch("default", 2048,
    2048//2, 44100)
# Set unit.
pDetection.set_unit("Hz")
pDetection.set_silence(-60)

plt.ion()

fig = plt.gcf()
fig.show()
fig.canvas.draw()

iteration = 0
plt.title('Color representation of the current input audio frequency')

while True:
	iteration += 1
	data = stream.read(1024, exception_on_overflow=False)
	samples = num.fromstring(data, dtype=aubio.float_type)
	pitch = pDetection(samples)[0]
	# Compute the energy (volume) of the
	# current frame.
	volume = num.sum(samples**2)/len(samples)
	# Format the volume output so that at most
	# it has six decimal numbers.
	volume = "{:.6f}".format(volume)	
	
	os.system('cls' if os.name == 'nt' else 'clear')
	print('Frequency: ' + str(pitch) + 'Hz')
	print('Volume: ' + str(volume))
	frequency = pitch
	wavelength = 700-((frequency*255/1000)+450)+450

	rgb = wavelength_to_rgb(wavelength)
	print('RGB: ' + str(rgb))

	#VIZUALIZATION
	spikes = np.random.random(1) #To show a rectangle
	print(spikes)

	plt.xlabel('Frequency: ' + str(round(float(pitch))) + 'Hz | Volume: ' + str(volume) + ' | Actual color (RGB): ' + str(rgb))

	plt.eventplot(spikes, orientation='horizontal', linelengths=0.9, linewidth=1000, color = [(rgb[0]/255, rgb[1]/255, rgb[2]/255)])	
	
	if iteration > 100:
		iteration = 0
		plt.clf()
		plt.title('Color representation of the current input audio frequency')
	
	fig.canvas.draw()
	plt.pause(0.000001)
