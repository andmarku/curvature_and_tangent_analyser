import numpy as np

# 5 ELEMENT CASE
''' Calculates the knutsson mapping of a vector

Input is on the form:
    numpy array: allEigenvectors = (dimX, dimY, dimZ, 3, 3)

Output is on the form:
    numpy array: allKnutsson = (dimX, dimY, dimZ,5)
'''

def knutssonMapping(eigenvector):
    # knutMap = np.outer(eigenvector,eigenvector)/np.linalg.norm(eigenvector)
    knutMap = np.zeros(5)
    knutMap[0] = eigenvector[0]*eigenvector[0] - eigenvector[1]*eigenvector[1]
    knutMap[1] = 2*eigenvector[0]*eigenvector[1]
    knutMap[2] = 2*eigenvector[0]*eigenvector[2]
    knutMap[3] = 2*eigenvector[1]*eigenvector[2]
    knutMap[4] = (2*eigenvector[2]*eigenvector[2] -eigenvector[0]*eigenvector[0] - eigenvector[1]*eigenvector[1])/np.sqrt(3)
    knutMap = knutMap/np.linalg.norm(eigenvector)
    return knutMap

def knutssonMapper(allEigenvectors):
    dim = allEigenvectors.shape
    allKnutsson = np.zeros((dim[0],dim[1],dim[2],5))

    # add all knutsson vectors to matrix, and if eigenvector i zero, add zero vector
    for idx, _ in np.ndenumerate(allEigenvectors[:,:,:,0]):
        voxelEig = allEigenvectors[idx[0], idx[1], idx[2], :]
        if(not np.any(allEigenvectors[idx[0], idx[1], idx[2],:])):
            allKnutsson[idx[0], idx[1], idx[2],:] = np.zeros(5)
        else:
            allKnutsson[idx[0], idx[1], idx[2],:] = knutssonMapping(allEigenvectors[idx[0], idx[1], idx[2],:])


    return allKnutsson
