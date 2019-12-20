import numpy as np

def dmDotTangents(tensor_knutVecs, tensor_tangents):
    ''' Dot product of DM matrix and tangent vectors in each voxel.

    Parameters
    ---------
    tensor_knutVecs : the flattened Knutsson vector in each voxel, N x M x L x 9.

    tensor_tangents : tangent vectors in each voxel N x M x L x 3.

    Returns
    -------
    vector of floats
        dmAlongTangent : derivatives of flattened Knuttson vector, N x M x L x 9.
    '''
    tensor_DM = approximateAlong_XYZ(tensor_knutVecs)

    dim = tensor_knutVecs.shape
    dmAlongTangent = np.zeros((dim[0],dim[1],dim[2],9))

    # for each DM take the dot product between the 3 derivatives and the tangent
    for idx, _ in np.ndenumerate(tensor_DM[:,:,:,0,0]):
        voxelDM = tensor_DM[idx[0], idx[1], idx[2], :, :]
        voxelTangent = tensor_tangents[idx[0], idx[1], idx[2],:]
        dmAlongTangent[idx[0], idx[1], idx[2],:] = voxelTangent@voxelDM

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
