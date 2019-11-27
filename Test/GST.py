import numpy as np
from GST0 import calculateGST0
from scipy.ndimage import gaussian_filter
from scipy.ndimage import gaussian_filter1d

''' Uniform weights matrix '''
def getWeights(window_size):
    return np.ones((window_size, window_size, window_size)) / window_size ** 3

''' Mirrors indices over matrix borders '''
def getMirror(matrix, indices):

    mirror = np.zeros(len(indices), dtype='int')

    for dim, index in enumerate(indices):

        mirror[dim] = index

        if index < 0:
            mirror[dim] = -mirror[dim]
        elif index > matrix.shape[dim] - 1:
            mirror[dim] = 2*(matrix.shape[dim] - 1) - mirror[dim]

    return matrix[tuple(mirror)]

''' Calculates the gradient structure tensor '''
def calculateGST(partials, window_size):

    GST = np.zeros(partials.shape + (3,))
    weights = getWeights(window_size)

    for (x, y, z, i, j), g in np.ndenumerate(GST):
        for (dx, dy, dz), w in np.ndenumerate(weights):
            S1 = getMirror(partials[:,:,:,i], (x+dx, y+dy, z+dz))
            S2 = getMirror(partials[:,:,:,j], (x+dx, y+dy, z+dz))
            GST[x,y,z,i,j] = GST[x,y,z,i,j] + w * S1 * S2

    return GST

if __name__ == '__main__':
    random_array = np.random.rand(10, 10, 10, 3)
    GST = calculateGST(random_array, 3)

    print("GST:", GST[0,0,0,:,:])

    GST0 = calculateGST0(random_array, 3)

    print("GST0:", GST0[0,0,0,:,:])
