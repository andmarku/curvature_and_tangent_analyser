import numpy as np
# from dw_dt_approximator import centralDifferenceVector
from scipy.ndimage import gaussian_filter1d


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
                # currentKnutVec =knutsonVec[x,y,z,:]
                # Loop for elements in knutsson vector
                for elementInKnut in range(9):
                    tensor_DM[:,y,z,0,elementInKnut] = centralDifferenceVector(knutVecs[:,y,z,elementInKnut])
                    tensor_DM[x,:,z,1,elementInKnut] = centralDifferenceVector(knutVecs[x,:,z,elementInKnut])
                    tensor_DM[x,y,:,2,elementInKnut] = centralDifferenceVector(knutVecs[x,y,:,elementInKnut])

    return tensor_DM


def convolution(knutVecs, sig = 1000):
    dim = knutVecs.shape
    tensor_DM = np.zeros((dim[0],dim[1],dim[2],3,9))

    for elementInKnut in range(9):
        tensor_DM[:,:,:,0,elementInKnut] = gaussian_filter1d(knutVecs[:,:,:,elementInKnut], sigma=sig, order = 1, axis = 0, mode='mirror', truncate = 0.001)
        tensor_DM[:,:,:,1,elementInKnut] = gaussian_filter1d(knutVecs[:,:,:,elementInKnut], sigma=sig, order = 1, axis = 1, mode='mirror', truncate = 0.001)
        tensor_DM[:,:,:,2,elementInKnut] = gaussian_filter1d(knutVecs[:,:,:,elementInKnut], sigma=sig, order = 1, axis = 2, mode='mirror', truncate = 0.001)

    return tensor_DM

def multiDiffW(knutVecs):
    dim = knutVecs.shape
    tensor_DM = np.zeros((dim[0],dim[1],dim[2],3,9))

    for elementInKnut in range(9):
        tensor_DM[:,:,:,0,elementInKnut] = np.gradient(knutVecs[:,:,:,elementInKnut], axis = 0)
        tensor_DM[:,:,:,1,elementInKnut] = np.gradient(knutVecs[:,:,:,elementInKnut], axis = 1)
        tensor_DM[:,:,:,2,elementInKnut] = np.gradient(knutVecs[:,:,:,elementInKnut], axis = 2)

    return tensor_DM

if __name__ == '__main__':
    knutsonVec = np.random.rand(200,200,200,9)
    # print(knutsonVec.shape)
    # oldDiff = approximateAlong_XYZ(knutsonVec)
    # newDiff = convolution(knutsonVec)
    # newDiff = multiDiffW(knutsonVec)
    test = np.array([1,2,3])
    print(test.dot(test))
    # print(centralDifferenceVector(squaredData))
    # print(multiDiffW(knutsonVec)[0,0,0,0,:])
    # import pdb; pdb.set_trace()
    # print(oldDiff[0,0,0,0,:])
    # print(newDiff.shape)
    # print(oldDiff == newDiff)
    # print(knutsonVec)
    # print(knutsonVec[1,1,:,1])
    # print(knutsonVec[1,1,1,:])
    # print(centralDifferenceVector(knutsonVec[1,1,1,:]))
    # for idx, value in np.ndenumerate(knutsonVec):
    #     print('index: ',idx, 'value: ', value, 'knut in x: ', knutsonVec[:,idx[1], idx[2],:])
