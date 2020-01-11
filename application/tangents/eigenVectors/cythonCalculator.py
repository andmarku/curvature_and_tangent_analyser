import numpy as np
import cython_eigenFunction as cython

def calculateWithCython(GST):
    print("calculating eigenvectors")

    data = np.zeros((GST.shape[0], GST.shape[1], GST.shape[2], 3))
    for (i, j, k), m in np.ndenumerate(GST[:,:,:,0,0]):
        if( np.any(GST[i,j,k,:,:])):
            data[i,j,k,:] = cython.calculateTangent(GST[i,j,k,:,:])

    print("finished eigenvalues")

    return data
