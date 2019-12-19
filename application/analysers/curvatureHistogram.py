import numpy as np
import matplotlib.mlab as mlab
from scipy.stats import norm
import matplotlib.pyplot as plt

def createCurvatureHistogram(tensor_curvatures):
    curvatures = tensor_curvatures.flatten()

    curvatures_without_zeros = curvatures[curvatures != 0]

    num_bins = 20
    # the histogram of the data
    n, bins, patches = plt.hist(curvatures_without_zeros, num_bins, density=1, facecolor='blue', alpha=0.5)

    plt.xlabel('Curvature')
    plt.ylabel('Probability')
    plt.title(r'Histogram of curvature: figure rsl, fiber width $=1$')

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.show()
