import numpy as np
from scipy.ndimage import gaussian_filter

''' Calculates the gradient structure tensor

Input is on the form:
    numpy array: partials = (N1, N2, N3, 3)
    real value: std

Output is on the form:
    numpy array: GST = (N1, N2, N3, 3, 3)
'''
def calculateGST0(partials, std):

    GST = np.zeros(partials.shape + (partials.shape[3],))

    for (i, j), _ in np.ndenumerate(GST[0,0,0,:,:]):
        structure = partials[:,:,:,i] * partials[:,:,:,j]
        GST[:,:,:,i,j] = gaussian_filter(structure, sigma=std, mode='constant', truncate=3)

    return GST
