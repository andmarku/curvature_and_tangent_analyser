import numpy as np
import scipy.linalg as sp

def calculateWithEigh(GST):
    print("calculating eigenvectors")

    dims = (GST.shape[0], GST.shape[1], GST.shape[2])
    data = np.zeros((GST.shape[0], GST.shape[1], GST.shape[2], 3))
    for (i, j, k), m in np.ndenumerate(GST[:,:,:,0,0]):
        if(np.any(GST[i,j,k,:,:])):
            eigs, vecs = np.linalg.eigh(GST[i,j,k,:,:])

            nonzero_eigs = eigs[eigs.nonzero()]
            nonzero_vecs = vecs[:, eigs.nonzero()[0]]

            index = np.argmin(abs(nonzero_eigs))

            data[i,j,k,:] = nonzero_vecs[:, index]

    print("finished eigenvalues")

    return data
