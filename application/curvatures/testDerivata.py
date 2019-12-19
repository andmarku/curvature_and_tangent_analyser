import numpy as np
from dw_dt_approximator import centralDifferenceVector

def approximateAlong_XYZ(knutVecs):
    '''Numerical spacial differentiation of knutsson for every voxel.

    Parameters
    ---------
    knutVecs : knutsson for every voxel, assumes knutVecs are N x M x L x 9.

    Returns
    -------
    vector of floats
        tensor_DM : dimensions N x M x L x 3 x 9.
                    N, M, L are the 3 dimensional space coordinates.
                    3 x 9 are the dimension of the local DM matrix.

    '''
    dim = knutVecs.shape
    tensor_DM = np.zeros((dim[0],dim[1],dim[2],3,9))

    # derive along x-space
    for y in range(dim[1]):
        for z in range(dim[2]):
            # for each element in the transformed vector
            for i in range(9):
                tensor_DM[:,y,z,0,i] = centralDifferenceVector(knutVecs[:,y,z,i])

    # derive along y-space
    for x in range(dim[0]):
        for z in range(dim[2]):
            # for each element in the transformed vector
            for i in range(9):
                tensor_DM[x,:,z,1,i] = centralDifferenceVector(knutVecs[x,:,z,i])

    # derive along z-space
    for x in range(dim[0]):
        for y in range(dim[1]):
            # for each element in the transformed vector
            for i in range(9):
                tensor_DM[x,y,:,2,i] = centralDifferenceVector(knutVecs[x,y,:,i])

    return tensor_DM

def voxelDiff(knutVecs):
    dim = knutVecs.shape
    tensor_DM = np.zeros((dim[0],dim[1],dim[2],3,9))

    # The first 3 outer loops are spaatial
    for z in range(dim[2]):
        for y in range(dim[1]):
            for x in range(dim[0]):
                # Loop for elements in knutsson vector
                for elementInKnut in range(9):
                    tensor_DM[x,y,z,0,elementInKnut] = centralDifferenceVector(knutVecs[:,y,z,elementInKnut])
                    tensor_DM[x,y,z,1,elementInKnut] = centralDifferenceVector(knutVecs[x,:,z,elementInKnut])
                    tensor_DM[x,y,z,2,elementInKnut] = centralDifferenceVector(knutVecs[x,y,:,elementInKnut])

    return tensor_DM


if __name__ == '__main__':
    knutsonVec = np.random.rand(2,2,2,9)
    # print(knutsonVec.shape)
    oldDiff = approximateAlong_XYZ(knutsonVec)
    newDiff = voxelDiff(knutsonVec)
    # print(oldDiff.shape)
    # print(newDiff.shape)
    print(oldDiff == newDiff)
    
