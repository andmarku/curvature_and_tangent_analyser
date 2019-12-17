import numpy as np

# define constant
CONST_SQRT_OF_TWO = np.sqrt(2)

def calcCurvatureForAllVoxels(tensor_dmAlongTangent):
    dim = tensor_dmAlongTangent.shape
    tensor_curvatures = np.zeros((dim[0],dim[1],dim[2]))

    # for each voxel, calculate the curvature
    for x in range(dim[0]):
        for y in range(dim[1]):
            for z in range(dim[2]):
                tensor_curvatures[x,y,z] = calcCurvature(dmAlongTangent[x,y,z,:])

    return tensor_curvatures

# calculate curvature for single voxel
def calcCurvature(dmAlongTangent):
    return CONST_SQRT_OF_TWO*np.linalg.norm(dmAlongTangent)
