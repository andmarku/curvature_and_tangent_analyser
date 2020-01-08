import numpy as np
import cython_eigenFunction as cython
import cython_eigenFunctionCopy as cythonCopy

def calculateWithCython(GST):
    print("calculating eigenvectors")

    # data = cythonCopy.calculateWithCython(GST)

    dims = (GST.shape[0], GST.shape[1], GST.shape[2])
    x_coord = np.zeros(dims)
    y_coord = np.zeros(dims)
    z_coord = np.zeros(dims)

    for (i, j, k), m in np.ndenumerate(GST[:,:,:,0,0]):
        if( GST[i,j,k,:,:].max() > 0.0001):
            nonzero_vecs = cython.calculateTangent(GST[i,j,k,:,:])
            x_coord[i,j,k] = nonzero_vecs[0]
            y_coord[i,j,k] = nonzero_vecs[1]
            z_coord[i,j,k] = nonzero_vecs[2]

    data = np.zeros((GST.shape[0], GST.shape[1], GST.shape[2], 3))
    data[:,:,:,0] = x_coord
    data[:,:,:,1] = y_coord
    data[:,:,:,2] = z_coord

    print("finished eigenvalues")

    return data
