from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np

def plotTangentComponents(tensor_tangents):
    dims =  tensor_tangents.shape
    x,y,z = np.meshgrid(np.arange(0,dims[0],1),np.arange(0,dims[1],1),np.arange(0,dims[2],1))

    xcomp = tensor_tangents[:,:,:,0]
    ycomp = tensor_tangents[:,:,:,1]
    zcomp = tensor_tangents[:,:,:,2]

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    plt.xlabel('x')
    plt.ylabel('y')

    # Plot x xomponents only
    ax.quiver(x, y, z, xcomp, ycomp, zcomp)
    plt.show()
