import numpy as np
from scipy.ndimage import gaussian_filter1d
from random import randint
import random
import readerMethod
import multiprocessing as mp
from multiprocessing.pool import ThreadPool


# Compute derivates with convolution
def convolution(input, sig, ax):
    Ix = gaussian_filter1d(input, sigma=sig, order = 1, axis = ax, mode='constant', truncate = 3*sig)
    # Iy = gaussian_filter1d(input, sigma=sig, order = 1, axis = 1, mode='constant', truncate = 3*sig)
    # Iz = gaussian_filter1d(input, sigma=sig, order = 1, axis = 2, mode='constant', truncate = 3*sig)
    return Ix
    # , Iy, Iz

if __name__== "__main__":
  input = readerMethod.readVTK('input.vtk')[0].astype('float')
  # A = convolution(input)
  pool = ThreadPool(mp.cpu_count())
  # results = pool.map(convolution, [row for row in input])
  results = [pool.apply(convolution, args=(input,2, ax)) for ax in range(0,2)]
  pool.close()
  # print(results)
  # print(results[0])
