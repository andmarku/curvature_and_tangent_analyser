import numpy as np

''' Calculates the smallest eigenvalue with corresponding eigenvector from GST

Input is on the form:
    numpy array: GST = (dimX, dimY, dimZ ,3, 3)

Output is on the form:
    numpy array: smallestEig = (dimX, dimY, dimZ)
    numpy array: eigenvectors = (dimX*dimY*dimZ,3)

'''

def eigCalc(GST):
    x_coordVec = np.zeros((GST.shape[0], GST.shape[1], GST.shape[2]))
    y_coordVec = np.zeros((GST.shape[0], GST.shape[1], GST.shape[2]))
    z_coordVec =np.zeros((GST.shape[0], GST.shape[1], GST.shape[2]))
    smallestEig = np.zeros((GST.shape[0], GST.shape[1], GST.shape[2]))
    eigenvectors = np.zeros((GST.shape[0]*GST.shape[1]*GST.shape[2], 3))

    for (i, j, k), m in np.ndenumerate(GST[:,:,:,0,0]):
        eigs, vecs = np.linalg.eigh(GST[i,j,k,:,:])
        index = np.argmin(abs(eigs))
        smallestEig[i,j,k] = eigs[index]
        x_coordVec[i,j,k] = vecs[0, index]
        y_coordVec[i,j,k] = vecs[1, index]
        z_coordVec[i,j,k] = vecs[2, index]

    x_coordVec = x_coordVec.flatten()
    y_coordVec = y_coordVec.flatten()
    z_coordVec = z_coordVec.flatten()

    eigenvectors[:, 0] = x_coordVec
    eigenvectors[:, 1] = y_coordVec
    eigenvectors[:, 2] = z_coordVec

    return smallestEig, eigenvectors
