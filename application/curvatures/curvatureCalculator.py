import numpy as np
import cython_calcCurvature as cython

def calcCurvatureForAllVoxels(tensor_dmAlongTangent):
    dim = tensor_dmAlongTangent.shape
    tensor_curvatures = np.zeros((dim[0],dim[1],dim[2]))

    # for each voxel, calculate the curvature
    for idx, _ in np.ndenumerate(tensor_curvatures):

        # cython optimization
        tensor_curvatures[idx[0], idx[1], idx[2]] = cython.calcCurvature(tensor_dmAlongTangent[idx[0], idx[1], idx[2],:])

    return tensor_curvatures
