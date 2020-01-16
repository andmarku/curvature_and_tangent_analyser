import numpy as np

# define constant
CONST_SQRT_OF_TWO = np.sqrt(2)

def calcCurvatureForAllVoxels(tensor_dmAlongTangent):
    dim = tensor_dmAlongTangent.shape
    tensor_curvatures = np.zeros((dim[0],dim[1],dim[2]))

    # for each voxel, calculate the curvature
    for idx, _ in np.ndenumerate(tensor_curvatures):

        tensor_curvatures[idx[0], idx[1], idx[2]] =  calcCurvature(tensor_dmAlongTangent[idx[0], idx[1], idx[2],:])

    return tensor_curvatures

# calculate curvature for single voxel
def calcCurvature(dmAlongTangent):
    return np.linalg.norm(dmAlongTangent)/CONST_SQRT_OF_TWO
