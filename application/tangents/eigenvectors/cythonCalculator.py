import numpy as np
import cython_eigenFunction as cython

def calculateWithCython(GST):
    data = np.zeros((GST.shape[0], GST.shape[1], GST.shape[2], 3))
    for (i, j, k), m in np.ndenumerate(GST[:,:,:,0,0]):
        data[i,j,k,:] = cython.calculateTangent(GST[i,j,k,:,:])

    return data
