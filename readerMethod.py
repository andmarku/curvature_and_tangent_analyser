import numpy as np
# import scipy.linalg as sp
import pdb
from vtk import vtkStructuredPointsReader
from vtk.util import numpy_support as VN
# from GST0 import calculateGST0
# from gaussianSmoothing import convolution
# import matplotlib.pyplot as plt
# from physt import special


def readVTK(filename = 'input.vtk'):

    reader = vtkStructuredPointsReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    data = reader.GetOutput()
    dim = data.GetDimensions()

    # import pdb; pdb.set_trace()

    dataset = VN.vtk_to_numpy(data.GetPointData().GetArray(0))
    dataset = dataset.reshape(dim, order='F')

    nonzero_element_coordinates = dataset.nonzero()
    x, y, z = nonzero_element_coordinates

    return dataset, x, y, z

    # import matplotlib.pyplot as plt
    # from mpl_toolkits.mplot3d import Axes3D
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(x, y, z, zdir='z', c= 'red', s=1)
    # plt.show()

    # pdb.set_trace()

# if __name__ == '__main__':
#
#     d, x, y, z = readVTK()
#     Ix, Iy, Iz = convolution(d)
#
#     A = np.zeros(d.shape + (3,))
#
#     A[:,:,:,0] = Ix
#     A[:,:,:,1] = Iy
#     A[:,:,:,2] = Iz
#
#     GST = calculateGST0(A, 1)
#
#     x_coord = np.zeros((200, 200, 200))
#     y_coord = np.zeros((200, 200, 200))
#     z_coord = np.zeros((200, 200, 200))
#
#     for (i, j, k), m in np.ndenumerate(GST[:,:,:,0,0]):
#         #eigs, vecs = sp.eig(GST[i,j,k,:,:])
#         eigs, vecs = np.linalg.eig(GST[i,j,k,:,:])
#         index = np.argmin(abs(eigs))
#         x_coord[i,j,k] = vecs[0, index]
#         y_coord[i,j,k] = vecs[1, index]
#         z_coord[i,j,k] = vecs[2, index]
#     '''
#     data = np.zeros((200*200*200, 3))
#
#     x_coord = x_coord.flatten()
#     y_coord = y_coord.flatten()
#     z_coord = z_coord.flatten()
#
#     data[:, 0] = x_coord
#     data[:, 1] = y_coord
#     data[:, 2] = z_coord
#
#     spherical = np.zeros((200*200*200, 3))
#     hxy = np.hypot(data[:,0], data[:,1])
#     r = np.hypot(hxy, data[:,2])
#     el = np.arctan2(data[:,2], hxy)
#     az = np.arctan2(data[:,1], data[:,0])
#
#     #import pdb; pdb.set_trace()
#
#     spherical[:,0] = r
#     spherical[:,1] = el
#     spherical[:,2] = az
#
#     h = special.spherical_histogram(spherical)
#     globe = h.projection("theta", "phi")
#     # globe.plot()
#     globe.plot.globe_map(density=True, figsize=(7, 7), cmap="rainbow")
#     globe.plot.globe_map(density=False, figsize=(7, 7))
#     plt.show()
#     '''

    #import pdb; pdb.set_trace()

    #plt.hist(eigenvalues)
    #plt.show()
