import numpy as np
import matplotlib.mlab as mlab
from scipy.stats import norm
import matplotlib.pyplot as plt
# import sys
# sys.path.append('./data')

def createCurvatureHistogram(curvature, name_of_input, fiber_width, curvature_filename):
    ''' Function creating a histogram of sent in array with values

    Parameters
    ---------
    array with dimension m x 1

    '''
    num_bins = 40

    # Take out non-zero curvatures (only where there is a volume)
    nz_curvature = curvature[curvature.nonzero()]
    mean_curvature = nz_curvature.mean()

    # If no validation file exist, only one plot will be shown
    if not curvature_filename:
        # the histogram of the data
        n, bins, patches = plt.hist(nz_curvature, num_bins, density=1, facecolor='blue', alpha=0.5)

        plt.axvline(mean_curvature, c = 'red',label='Mean: ' + str(np.round(mean_curvature, 3)))
        plt.legend()
        plt.xlabel('Curvature')
        plt.ylabel('Frequency')
        title = 'Histogram of curvature: figure ' + name_of_input + \
         r', fiber width $=' + str(fiber_width) + r'$'
        plt.title(title)
    else:
        # path for validation file
        path = './data/' + str(curvature_filename)
        trueCurvatures = np.loadtxt(fname = path)
        # import pdb; pdb.set_trace()
        trueMean = np.mean(trueCurvatures)

        # the histogram of the data
        fig, axs = plt.subplots(1, 2, sharey=False, tight_layout=True)
        # n, bins, patches = plt.hist(nz_curvature, num_bins, density=1, facecolor='blue', alpha=0.5)
        n, bins, patches = axs[0].hist(nz_curvature, num_bins, density=1, facecolor='blue', alpha=0.5)
        axs[0].axvline(mean_curvature, c = 'red',label='Mean: ' + str(np.round(mean_curvature, 3)))
        axs[0].legend()
        axs[0].set_xlabel('Curvature')
        axs[0].set_ylabel('Frequency')
        title = 'Histogram of curvature: figure ' + name_of_input + \
         r', fiber width $=' + str(fiber_width) + r'$'
        axs[0].title.set_text(title)

        # True curvatures
        axs[1].hist(trueCurvatures, num_bins, density=1, facecolor='blue', alpha=0.5)
        axs[1].axvline(trueMean, c = 'red', label='True mean: ' + str(np.round(trueMean, 3)))
        axs[1].legend()
        title2 = 'Histogram of true curvature: figure ' + name_of_input + \
         r', fiber width $=' + str(fiber_width) + r'$'
        axs[1].title.set_text(title2)
        axs[1].set_xlabel('Curvature')
        axs[1].set_ylabel('Frequency')

        # Tweak spacing to prevent clipping of ylabel
        # plt.subplots_adjust(left=0.15)
    # plt.savefig("curvatures.png")
    plt.show()
        #import pdb; pdb.set_trace()
