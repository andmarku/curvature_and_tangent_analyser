import numpy as np

def dmDotTangents(tensor_knutVecs, tensor_tangents):
    tensor_DM = approximateAlong_XYZ(tensor_knutVecs)

    dim = tensor_knutVecs.shape
    dmAlongTangent = np.zeros((dim[0],dim[1],dim[2],9))

    # for each DM take the dot product between the 3 derivatives and the tangent
    for x in range(dim[0]):
        for y in range(dim[1]):
            for z in range(dim[2]):
                for i in range(9):
                    dmAlongTangent[x,y,z,i] = tensor_DM[x,y,z,:,i].dot(tensor_tangents[x,y,z])

    return dmAlongTangent

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
    for x in range(dim[1]):
        for y in range(dim[2]):
            # for each element in the transformed vector
            for i in range(9):
                tensor_DM[x,y,:,2,i] = centralDifferenceVector(knutVecs[x,y,:,i])

    return tensor_DM

def centralDifferenceVector(myVec):
    '''Central difference formula for n x 1 vectors.

    Parameters
    ---------
    myVec : n times 1 vector

    Returns
    -------
    vector of floats
        calculatedElements : calculatedElements[i] = (myVec[i+1] - myVec[i - 1])/2

    '''
    calculatedElements = np.zeros((myVec.size))

    # special case for first element: the second minus the first
    diff = (myVec[1] - myVec[0])
    calculatedElements[0] = diff

    # central difference for all elements along axis except first and last
    for i in range(1, (myVec.size -1)):
        diff  = (myVec[i+1] - myVec[i - 1])/2
        calculatedElements[i] = diff

    # special case for last element: the last element minus the second to last
    diff = (myVec[myVec.size -1] - myVec[myVec.size-2])
    calculatedElements[myVec.size-1] = diff

    return calculatedElements
