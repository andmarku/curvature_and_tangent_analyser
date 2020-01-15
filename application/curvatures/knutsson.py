import numpy as np
import cython_knutsson as cython

# 9 ELEMENT CASE

''' Calculates the knutsson mapping of a vector

Input is on the form:
    numpy array: allEigenvectors = (dimX, dimY, dimZ, 3, 3)

Output is on the form:
    numpy array: allKnutsson = (dimX, dimY, dimZ,9)
'''

def knutssonMapping(eigenvector):
    knutMap = np.outer(eigenvector,eigenvector)
    return knutMap.flatten()

def knutssonMapper(allEigenvectors):
    dim = allEigenvectors.shape
    allKnutsson = np.zeros((dim[0],dim[1],dim[2],9))

    # add all knutsson vectors to matrix, and if eigenvector i zero, add zero vector
    for idx, _ in np.ndenumerate(allEigenvectors[:,:,:,0]):
        # cython optimisation
        allKnutsson[idx[0], idx[1], idx[2],:] = cython.knutMap(allEigenvectors[idx[0], idx[1], idx[2],:])
        #
        # voxelEig = allEigenvectors[idx[0], idx[1], idx[2], :]
        # if(not np.any(allEigenvectors[idx[0], idx[1], idx[2],:])):
        #     allKnutsson[idx[0], idx[1], idx[2],:] = np.zeros(9)
        # else:
        #     allKnutsson[idx[0], idx[1], idx[2],:] = knutssonMapping(allEigenvectors[idx[0], idx[1], idx[2],:])


    return allKnutsson
