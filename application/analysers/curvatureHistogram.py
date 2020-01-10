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
    num_bins = 20
    # the histogram of the data
    n, bins, patches = plt.hist(curvature, num_bins, density=1, facecolor='blue', alpha=0.5)

    plt.xlabel('Curvature')
    plt.ylabel('Probability')
    title = 'Histogram of curvature: figure ' + name_of_input + \
     r', fiber width $=' + str(fiber_width) + r'$'
    plt.title(title)

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.savefig("curvatures.png")
    plt.show()
