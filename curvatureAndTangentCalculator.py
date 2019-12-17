import numpy as np
from readerMethod import readVTK
from gaussianSmoothing import convolution
from GST0 import calculateGST0
from eigenCalc import eigCalc
from knutsson import knutssonMapping
from curvature import curvatureCalculator

# if __name__ == '__main__':
def main():
    # Vtk data and positions of nonzero elements
    d, x, y, z = readVTK()
    # d = np.random.randint(1,101,27).reshape((3,3,3))
    # d = np.random.choice([0, 1], size=(27,), p=[1./9, 8./9]).reshape((3,3,3))

    # Gaussian smoothing of the data
    partials = convolution(d)

    # Calculates structure tensor
    GST = calculateGST0(partials, 1)

    # Computes eigenvalues and eigen vectors
    eigenvalues, eigenvectors =  eigCalc(GST)

    # Make Knutsson mapping and calculate corresponding curvature
    knutVectors = np.zeros((eigenvectors.shape[0], 9))
    curvatures = np.zeros(eigenvalues.shape).flatten()
    for i in range(0,len(eigenvectors)):
        knutVectors[i] = knutssonMapping(eigenvectors[i])
        curvatures[i] = curvatureCalculator(knutVectors[i],eigenvalues.flatten()[i])

    print('Done2!')
    # Reshape curvatures vector such that we get voxels
    # curvatures = curvatures.reshape(eigenvalues.shape)

    # print(curvatures)
    return curvatures, eigenvectors
    # TODO Write tangents (= eigenvectors) to file...

    # TODO Write curvatures to file...
