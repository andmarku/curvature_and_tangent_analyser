from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np

def plotTangentComponents(tensor_tangents):
    dims =  tensor_tangents.shape
    nonZeroTangents = tensor_tangents.nonzero()
    x,y,z = np.meshgrid(np.arange(0,dims[0],1),np.arange(0,dims[1],1),np.arange(0,dims[2],1))

    xcomp = tensor_tangents[:,:,:,0]
    ycomp = tensor_tangents[:,:,:,1]
    zcomp = tensor_tangents[:,:,:,2]
    # nz_xcomp = nonZeroTangents[:,:,:,0]
    # nz_ycomp = nonZeroTangents[:,:,:,1]
    # nz_zcomp = nonZeroTangents[:,:,:,2]

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    plt.xlabel('x')
    plt.ylabel('y')

    # # Plot x xomponents only
    # ycomp = np.zeros(xcomp.shape)
    # zcomp = np.zeros(xcomp.shape)
    ax.quiver(x, y, z, xcomp, ycomp, zcomp)
    # ax.quiver(x, y, z, nz_xcomp, nz_ycomp, nz_zcomp)
    plt.show()
    import pdb; pdb.set_trace()
