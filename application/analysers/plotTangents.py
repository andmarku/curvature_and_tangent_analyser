from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def plotTangentComponents(tensor_tangents):
    dims =  tensor_tangents.shape
    # x,y,z = np.meshgrid(np.arange(0,dims[0],1),np.arange(0,dims[1],1),np.arange(0,dims[2],1))
    x = tensor_tangents[:,:,:,0].shape[0]
    y = tensor_tangents[:,:,:,1].shape[1]
    z = tensor_tangents[:,:,:,2].shape[2]
    X,Y,Z = np.meshgrid(np.arange(0,x),np.arange(0,y),np.arange(0,z))

    xcomp = tensor_tangents[:,:,:,0]
    ycomp = tensor_tangents[:,:,:,1]
    zcomp = tensor_tangents[:,:,:,2]

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    plt.xlabel('x')
    plt.ylabel('y')

    # Plot x xomponents only
    ax.quiver(X,Y,Z, xcomp, ycomp, zcomp, alpha=0.8)
    fig.set_size_inches(16, 9)
    # plt.savefig("tangents.png")
    plt.show()
