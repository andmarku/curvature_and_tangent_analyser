import numpy as np
from knutsson import knutssonMapping


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

def knutsson2(allEigenvectors):
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

if __name__ == '__main__':
    allEigenvectors = np.random.rand(200,200,200,3)

    # old = knutssonMapper(allEigenvectors)
    new = knutsson2(allEigenvectors)
    # print(old[0,0,0,:])
    # print(new[0,0,0])
    # print(old==new)
