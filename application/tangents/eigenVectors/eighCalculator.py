import numpy as np
import scipy.linalg as sp

def calculateWithEigh(GST):
    print("calculating eigenvectors")

    dims = (GST.shape[0], GST.shape[1], GST.shape[2])
    data = np.zeros((GST.shape[0], GST.shape[1], GST.shape[2], 3))
    for (i, j, k), m in np.ndenumerate(GST[:,:,:,0,0]):
        if(np.any(GST[i,j,k,:,:])):
            eigs, vecs = np.linalg.eigh(GST[i,j,k,:,:])
            
            index = np.argmin(abs(eigs))

            data[i,j,k,:] = vecs[:, index]

    print("finished eigenvalues")

    return data
