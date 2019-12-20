import numpy as np
from curvatureHistogram import createCurvatureHistogram

def analyze(tensor_tangents, tensor_curvatures, name_of_input, fiber_width):
    # format input
    flattened_tangents = flatten_tangents(tensor_tangents)
    flattened_curvatures = tensor_curvatures.flatten()

    # find elements corresponding to smoothed fibers
    whichTangentsAreNonZero = np.any(flattened_tangents, axis=1)
    nonzero_tangents = flattened_tangents[whichTangentsAreNonZero != 0, :]
    curvatures_corr_to_nonzero_tangents = flattened_curvatures[whichTangentsAreNonZero != 0]

    print("Shape of flattened tangent tensor")
    print(flattened_tangents.shape)

    print("Shape of flattened curvature tensor")
    print(flattened_curvatures.shape)

    print("Number of tangents that are non zero")
    print(nonzero_tangents.shape)

    createCurvatureHistogram(curvatures_corr_to_nonzero_tangents, name_of_input, fiber_width)


def flatten_tangents(tensor_tangents):
    ''' Function for flattening the voxel space, while keeping the tangents

    Parameters
    ---------
    the tensor with each voxels tangent. Input should have dimension  X x Y x Z x 3,
    where X x Y x Z describes the dimension of the voxel space, and where 3 is
    the dimension of the tangent.

    Returns
    -------
    array with all tangents, with dimension XYZ x 3.

    '''
    dim_tangents = tensor_tangents.shape
    flattened_tangents = np.zeros((dim_tangents[0]*dim_tangents[1]*dim_tangents[2],3))
    flattened_tangents[:,0] = tensor_tangents[:,:,:,0].flatten()
    flattened_tangents[:,1] = tensor_tangents[:,:,:,1].flatten()
    flattened_tangents[:,2] = tensor_tangents[:,:,:,2].flatten()
    return flattened_tangents
