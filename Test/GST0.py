import numpy as np
from scipy.ndimage import gaussian_filter

''' Calculates the gradient structure tensor '''
def calculateGST0(partials, std):

    GST = np.zeros(partials.shape + (partials.shape[3],))

    for (i, j), _ in np.ndenumerate(GST[0,0,0,:,:]):
        structure = partials[:,:,:,i] * partials[:,:,:,j]
        GST[:,:,:,i,j] = gaussian_filter(structure, sigma=std, mode='constant')

    return GST
