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

    # for each DM take the dot product between the 3 derivatives and the tangent
    for x in range(dim[0]):
        for y in range(dim[1]):
            for z in range(dim[2]):
                allKnutsson[x,y,z,:] = knutssonMapping(allEigenvectors[x,y,z,:])

    return allKnutsson
