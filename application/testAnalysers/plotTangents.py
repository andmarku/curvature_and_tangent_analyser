from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def plotTangentComponents(tensor_tangents, fiber_width, name_of_input):
    '''Function that plots the orientation filed of the input

    Parameters:
        numpy array: tensor_tangents = (dimX, dimY, dimZ, 3) tensor of the tangents that builds the field
        scalar: fiber_with = radius of the fibers in the input
        string: name_of_input = file name of the input file

    Result:
        plot of the orientation field whih is saved to file 'name_of_input.png'

    '''

    dims =  tensor_tangents.shape
    x,y,z = np.meshgrid(np.arange(0,dims[0],1),np.arange(0,dims[1],1),np.arange(0,dims[2],1), indexing = 'ij')

    xcomp = tensor_tangents[:,:,:,0]
    ycomp = tensor_tangents[:,:,:,1]
    zcomp = tensor_tangents[:,:,:,2]

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_xlabel('$X$', fontsize=16)
    ax.set_ylabel('$Y$', fontsize=16)
    ax.set_zlabel('$Z$', fontsize=16)

    title = 'Orientation field of tangents: figure ' + name_of_input + \
     r', fiber radius $=' + str(fiber_width) + r'$'
    ax.set_title(title, size = 16)

    ax.quiver(x,y,z, xcomp, ycomp, zcomp, alpha=0.5)
    fig.set_size_inches(16, 9)

    # Save to file
    saveName = ''
    for char in name_of_input:
        if char != '.':
            saveName = saveName + char
        else:
            break
    plt.savefig(str(saveName)+"Tangents.png")
    plt.show()
