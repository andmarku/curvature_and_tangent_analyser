import numpy as np
from scipy.ndimage import gaussian_filter1d
from random import randint
import random

# Compute derivates with convolution
def convolution(input, sig = 1):
    Ix = gaussian_filter1d(input, sigma=sig, order = 1,axis = 0, mode='constant', truncate = 3*sig)
    Iy = gaussian_filter1d(input, sigma=sig, order = 1,axis = 1, mode='constant', truncate = 3*sig)
    Iz = gaussian_filter1d(input, sigma=sig, order = 1,axis = 2, mode='constant', truncate = 3*sig)
    return Ix, Iy, Iz

def main():
    # Test matrix
    # input = np.random.choice([0, 1], size=(200,200,200), p=[2./3, 1./3]).astype('float')
    input = np.random.rand(3,3,3).astype('float')
    A = convolution(input, sig = 2)
    print(A)

if __name__== "__main__":
  main()
