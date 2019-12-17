import numpy as np
from scipy.ndimage import gaussian_filter1d
from random import randint
import random

''' Calculates the gaussian smoothing of of the input matrix

Input is on the form:
    numpy array: input = (dimX, dimY, dimZ)

Output is on the form:
    tuple of numpy arrays: knutMap = ((dimX, dimY, dimZ), (dimX, dimY, dimZ), (dimX, dimY, dimZ))
'''

def convolution(input, sig = 1):
    Ix = gaussian_filter1d(input, sigma=sig, order = 1, axis = 0, mode='constant', truncate = 3*sig)
    Iy = gaussian_filter1d(input, sigma=sig, order = 1, axis = 1, mode='constant', truncate = 3*sig)
    Iz = gaussian_filter1d(input, sigma=sig, order = 1, axis = 2, mode='constant', truncate = 3*sig)

    partials = np.zeros(input.shape + (3,))

    partials[:,:,:,0] = Ix
    partials[:,:,:,1] = Iy
    partials[:,:,:,2] = Iz

    return partials