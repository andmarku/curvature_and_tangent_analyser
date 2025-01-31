import numpy as np
import cython_knutsson as cython

''' Calculates the knutsson mapping of a vector

Input is on the form:
    numpy array: allEigenvectors = (dimX, dimY, dimZ, 3, 3)

Output is on the form:
    numpy array: allKnutsson = (dimX, dimY, dimZ,9)
'''
def knutssonMapper(allEigenvectors):
    dim = allEigenvectors.shape
    allKnutsson = np.zeros((dim[0],dim[1],dim[2],9))

    # add all knutsson vectors to matrix, and if eigenvector i zero, add zero vector
    for idx, _ in np.ndenumerate(allEigenvectors[:,:,:,0]):
        allKnutsson[idx[0], idx[1], idx[2],:] = cython.knutMap(allEigenvectors[idx[0], idx[1], idx[2],:])

    return allKnutsson
