import numpy as np
import matplotlib.mlab as mlab
from scipy.stats import norm
import matplotlib.pyplot as plt

def createCurvatureHistogram(curvature, name_of_input, fiber_width):
    ''' Function creating a histogram of sent in array with values

    Parameters
    ---------
    array with dimension m x 1

    '''
    num_bins = 35

    # Take out non-zero curvatures (only where there is a volume)
    nz_curvature = curvature[curvature.nonzero()]
    mean_curvature = nz_curvature.mean()

    # the histogram of the data
    n, bins, patches = plt.hist(nz_curvature, num_bins, density=1, facecolor='blue', alpha=0.5)
    plt.axvline(mean_curvature, c = 'red',label='Mean: ' + str(np.round(mean_curvature, 3)))
    plt.legend()
    plt.xlabel('Curvature')
    plt.ylabel('Frequency')
    title = 'Histogram of curvature: figure ' + name_of_input + \
     r', fiber width $=' + str(fiber_width) + r'$'
    plt.title(title)

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.show()
    #import pdb; pdb.set_trace()
