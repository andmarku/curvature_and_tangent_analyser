import numpy
import pdb
from vtk import vtkStructuredPointsReader
from vtk.util import numpy_support as VN

filename = 'input.vtk'

reader = vtkStructuredPointsReader()
reader.SetFileName(filename)
reader.ReadAllVectorsOn()
reader.ReadAllScalarsOn()
reader.Update()

data = reader.GetOutput()
dim = data.GetDimensions()

dataset = VN.vtk_to_numpy(data.GetPointData().GetArray(0))
dataset = dataset.reshape(dim, order='F')
nonzero_element_coordinates = dataset.nonzero()
z, x, y = nonzero_element_coordinates

pdb.set_trace()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, zdir='z', c= 'red')
plt.show()

pdb.set_trace()
