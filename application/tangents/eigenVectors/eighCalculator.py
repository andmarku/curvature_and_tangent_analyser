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

            # make sure that the zero vector is returned if the geometric
            # multiplicity is larger than one
            eigVal = eigs[index]
            alternativeEigVals = np.delete(eigs, index)
            if(eigVal == alternativeEigVals[0]):
                egVec = vecs[:, index]
                alternativeEigVecs = np.delete(vecs, index,1)
                altEgVec = alternativeEigVecs[:,0]

                # eigh returns normalized vectors, so dividing by norm is't needed
                discrepancy =  1 - np.absolute(altEgVec.dot(egVec))
                if(discrepancy > 1e-10):
                    data[i,j,k,:] = np.zeros(3)
                else:
                    data[i,j,k,:] = vecs[:, index]
            elif(eigVal == alternativeEigVals[1]):
                egVec = vecs[:, index]
                alternativeEigVecs = np.delete(vecs, index,1)
                altEgVec = alternativeEigVecs[:,1]

                # eigh returns normalized vectors, so dividing by norm is't needed
                discrepancy =  1 - np.absolute(altEgVec.dot(egVec))
                if(discrepancy > 1e-10):
                    data[i,j,k,:] = np.zeros(3)
                else:
                    data[i,j,k,:] = vecs[:, index]
            else:
                data[i,j,k,:] = vecs[:, index]

    print("finished eigenvalues")

    return data
