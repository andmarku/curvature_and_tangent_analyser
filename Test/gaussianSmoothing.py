import numpy as np
from scipy.ndimage import gaussian_filter1d
from random import randint
import random
import readerMethod

# Compute derivates with convolution
def convolution(input, sig = 1):
    Ix = gaussian_filter1d(input, sigma=sig, order = 1, axis = 0, mode='constant', truncate = 3*sig)
    Iy = gaussian_filter1d(input, sigma=sig, order = 1, axis = 1, mode='constant', truncate = 3*sig)
    Iz = gaussian_filter1d(input, sigma=sig, order = 1, axis = 2, mode='constant', truncate = 3*sig)
    return Ix, Iy, Iz

if __name__== "__main__":
  input = readerMethod.readVTK('input.vtk')[0].astype('float')
  A = convolution(input, sig = 2)
  print(A)
