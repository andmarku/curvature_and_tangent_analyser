import numpy as np
from vtk.util import numpy_support as VN
import vtk
from vtk import vtkStructuredPointsWriter

def writeNow(input, filename):

    dimensions = input.shape

    array = VN.numpy_to_vtk(input.ravel(), deep=True, array_type=vtk.VTK_FLOAT)

    data = vtk.vtkPointData()
    data.AddArray(array)

    points = vtk.vtkStructuredPoints()
    points.SetDimensions(dimensions)
    points.SetFieldData(data)

    writer = vtkStructuredPointsWriter()

    writer.SetFileName(filename)

    writer.SetInputData(points)
    writer.Write()

    #stream = writer.OpenVTKFile()

    #data.SetDimensions(dimensions)

    #stream.WritePoints(data)

    print(data)

    #import pdb; pdb.set_trace()

def writeTest(input, filename):

    dimensions = input[:,:,:,0].shape

    array1 = VN.numpy_to_vtk(input[:,:,:,0].ravel(), deep=True, array_type=vtk.VTK_FLOAT)
    array2 = VN.numpy_to_vtk(input[:,:,:,1].ravel(), deep=True, array_type=vtk.VTK_FLOAT)
    array3 = VN.numpy_to_vtk(input[:,:,:,2].ravel(), deep=True, array_type=vtk.VTK_FLOAT)

    data = vtk.vtkPointData()
    data.AddArray(array1)
    data.AddArray(array2)
    data.AddArray(array3)

    points = vtk.vtkStructuredPoints()
    points.SetDimensions(dimensions)
    points.SetFieldData(data)

    writer = vtkStructuredPointsWriter()

    writer.SetFileName(filename)

    writer.SetInputData(points)
    writer.Write()

    #stream = writer.OpenVTKFile()

    #data.SetDimensions(dimensions)

    #stream.WritePoints(data)

    print(data)

    #import pdb; pdb.set_trace()

if __name__ == '__main__':

    A = np.random.rand(10,10,10)

    writeNow(A, 'curvature.vtk')

    B = np.random.rand(10,10,10,3)

    writeTest(B, 'tangent.vtk')
