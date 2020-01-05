import numpy as np
import scipy.linalg as sp

def  calculateEigenVectors(GST):
    print("calculating eigenvectors")
    dims = (GST.shape[0], GST.shape[1], GST.shape[2])
    x_coord = np.zeros(dims)
    y_coord = np.zeros(dims)
    z_coord = np.zeros(dims)

    for (i, j, k), m in np.ndenumerate(GST[:,:,:,0,0]):
        if(not np.any(GST[i,j,k,:,:])):
            x_coord[i,j,k] = 0
            y_coord[i,j,k] = 0
            z_coord[i,j,k] = 0
        else:

            eigs, vecs = np.linalg.eigh(GST[i,j,k,:,:])

            nonzero_eigs = eigs[eigs.nonzero()]
            nonzero_vecs = vecs[:, eigs.nonzero()]

            index = np.argmin(abs(nonzero_eigs))

            x_coord[i,j,k] = nonzero_vecs[0, 0, index]
            y_coord[i,j,k] = nonzero_vecs[1, 0, index]
            z_coord[i,j,k] = nonzero_vecs[2, 0, index]

    print("finished eigenvalues")
   
    data = np.zeros((GST.shape[0], GST.shape[1], GST.shape[2], 3))
    data[:,:,:,0] = x_coord
    data[:,:,:,1] = y_coord
    data[:,:,:,2] = z_coord

    return data
