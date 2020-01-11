import numpy as np

def filterSmoothedCurvatures(tensor_curvatures, tensor_tangents,x,y,z):
    nzCurvatures = np.zeros(tensor_curvatures.shape)
    nzTangents = np.zeros(tensor_tangents.shape)
    #import pdb; pdb.set_trace()
    nzCurvatures[x, y, z] = tensor_curvatures[x, y, z]
    nzTangents[x,y,z,:] = tensor_tangents[x,y,z,:]


    return nzCurvatures, nzTangents
