import numpy as np
import matplotlib.mlab as mlab
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib as mpl

def createCurvatureHistogram(curvature, name_of_input, fiber_width, curvature_filename):
    ''' Function creating a histogram of sent in array with values

    Parameters
    ---------
    array with dimension m x 1

    '''
    num_bins = 40

    mean_curvature = curvature.mean()

    # If no validation file exist, only one plot will be shown
    if not curvature_filename:
        # the histogram of the data
        plt.figure(figsize=(16, 9))
        n, bins, patches = plt.hist(curvature, num_bins, density=1, facecolor='blue', alpha=0.5)

        plt.axvline(mean_curvature, c = 'red',label='Mean: ' + str(np.round(mean_curvature, 3)))
        plt.legend(prop={"size":20})
        plt.xlabel('Curvature', size=16)
        plt.ylabel('Frequency', size=16)
        title = 'Histogram of curvature: figure ' + name_of_input + \
         r', fiber width $=' + str(fiber_width) + r'$'
        plt.title(title, size=16)
        # Tweak spacing to prevent clipping of ylabel
        plt.subplots_adjust(left=0.15)
        plt.savefig("curvatures.png")
    else:
        # path for validation file
        path = './data/testfiles/' + curvature_filename

        trueCurvatures = np.loadtxt(fname = path)
        trueMean = np.mean(trueCurvatures)

        # the histogram of the data
        fig, axs = plt.subplots(1, 2, sharey=False, tight_layout=True)
        n, bins, patches = axs[0].hist(curvature, num_bins, density=1, facecolor='blue', alpha=0.5)
        axs[0].axvline(mean_curvature, c = 'red',label='Mean: ' + str(np.round(mean_curvature, 3)))
        axs[0].legend(prop={"size":20})
        axs[0].set_xlabel('Curvature', size=16)
        axs[0].set_ylabel('Frequency', size=16)
        title = 'Histogram of curvature: figure ' + name_of_input + \
         r', fiber radius $=' + str(fiber_width) + r'$'
        axs[0].set_title(title, size=16)

        # True curvatures
        axs[1].hist(trueCurvatures, num_bins, density=1, facecolor='blue', alpha=0.5)
        axs[1].axvline(trueMean, c = 'red', label='True mean: ' + str(np.round(trueMean, 3)))
        axs[1].legend(prop={"size":20})
        title2 = 'Histogram of true curvature: figure ' + name_of_input + \
         r', fiber radius $=' + str(fiber_width) + r'$'
        axs[1].set_title(title2, size=16)
        axs[1].set_xlabel('Curvature', size=16)
        axs[1].set_ylabel('Frequency', size=16)

        fig.set_size_inches(16, 9)
        plt.savefig(str(name_of_input)+"Curvatures.png")

    plt.show()
