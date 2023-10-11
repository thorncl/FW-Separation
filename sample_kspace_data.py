import numpy as np
from skimage.io import imread, imshow
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import pandas as pd

test_image = imread('brain_image.png')

plt.figure()
plt.imshow(test_image, cmap='gray')
plt.show()

fft = np.fft.fftshift(np.fft.fft2(test_image))

magnitude_spectrum = np.abs(fft)
phase_spectrum = np.angle(fft)




