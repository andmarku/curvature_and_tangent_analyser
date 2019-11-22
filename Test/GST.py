import numpy as np
import scipy.stats as stats

def weight(x, y, z, window_size):

    sp.stats.norm(loc = 0, scale = window_size/2)

def calculateGST(Ix=0, Iy=0, Iz=0, intensity=np.zeros((2,2,2)), window_size=3):

    GST = np.zeros(intensity.shape + (3,3))

    window = np.zeros((window_size, window_size, window_size))

    # z is changing first, the y and then x at the end.
    for (x, y, z), i in np.ndenumerate(intensity):
        for (dx, dy, dz), w in np.ndenumerate(window):

            print((x + dx, y + dy, z + dz))

if __name__ == '__main__':
    calculateGST()
