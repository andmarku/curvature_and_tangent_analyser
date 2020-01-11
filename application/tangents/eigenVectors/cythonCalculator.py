import numpy as np
import cython_eigenFunction as cython

def calculateWithCython(GST):
    print("calculating eigenvectors")

    data = np.zeros((GST.shape[0], GST.shape[1], GST.shape[2], 3))
    for (i, j, k), m in np.ndenumerate(GST[:,:,:,0,0]):
        if( GST[i,j,k,:,:].max() > 0.0001):
            data[i,j,k,:] = cython.calculateTangent(GST[i,j,k,:,:])
        elif(np.any(GST[i,j,k,:,:])):
            eigs, vecs = np.linalg.eigh(GST[i,j,k,:,:])
            index = np.argmin(abs(eigs))
            data[i,j,k,:] = vecs[:, index]

    print("finished eigenvalues")

    return data
