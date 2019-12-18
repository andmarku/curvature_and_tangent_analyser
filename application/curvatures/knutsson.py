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
    for x in range(dim[0]):
        for y in range(dim[1]):
            for z in range(dim[2]):
                if(not np.any(allEigenvectors[x,y,z,:])):
                    allKnutsson[x,y,z,:] = np.zeros(9)
                else:
                    allKnutsson[x,y,z,:] = knutssonMapping(allEigenvectors[x,y,z,:])

    return allKnutsson
