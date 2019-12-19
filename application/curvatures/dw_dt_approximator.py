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

    for elementInKnut in range(9):
        tensor_DM[:,:,:,0,elementInKnut] = np.gradient(knutVecs[:,:,:,elementInKnut], axis = 0)
        tensor_DM[:,:,:,1,elementInKnut] = np.gradient(knutVecs[:,:,:,elementInKnut], axis = 1)
        tensor_DM[:,:,:,2,elementInKnut] = np.gradient(knutVecs[:,:,:,elementInKnut], axis = 2)

    return tensor_DM
