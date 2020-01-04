import numpy as np

''' Calculates the knutsson mapping of a vector

Input is on the form:
    numpy array: eigenvector = (3, 3)

Output is on the form:
    numpy array: knutMap = (9,1)
'''

def knutssonMapping(eigenvector):
    knutMap = np.outer(eigenvector,eigenvector)/np.linalg.norm(eigenvector)
    return knutMap.flatten()

def knutssonMapper(allEigenvectors):
    dim = allEigenvectors.shape
    allKnutsson = np.zeros((dim[0],dim[1],dim[2],9))

    # add all knutsson vectors to matrix, and if eigenvector i zero, add zero vector
    for idx, _ in np.ndenumerate(allEigenvectors[:,:,:,0]):
        voxelEig = allEigenvectors[idx[0], idx[1], idx[2], :]
        if(not np.any(allEigenvectors[idx[0], idx[1], idx[2],:])):
            allKnutsson[idx[0], idx[1], idx[2],:] = np.zeros(9)
        else:
            allKnutsson[idx[0], idx[1], idx[2],:] = knutssonMapping(allEigenvectors[idx[0], idx[1], idx[2],:])


    return allKnutsson
