import numpy as np
from vtk.util import numpy_support as VN
import vtk
from vtk import vtkStructuredPointsWriter

def writeNow(input, filename):

    dimensions = input.shape

    array = VN.numpy_to_vtk(input.ravel(), deep=True, array_type=vtk.VTK_FLOAT)

    points = vtk.vtkStructuredPoints()
    points.SetDimensions(dimensions)
    points.GetPointData().AddArray(array)

    writer = vtkStructuredPointsWriter()
    writer.SetFileTypeToBinary()
    writer.SetFileName(filename)
    writer.SetInputData(points)

    import pdb; pdb.set_trace()

    writer.Write()

    #stream = writer.OpenVTKFile()

    #data.SetDimensions(dimensions)

    #stream.Wri

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

def importTest(filename):

    reader = vtk.vtkStructuredPointsReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    data = reader.GetOutput()
    dim = data.GetDimensions()

    import pdb; pdb.set_trace()

    dataset = VN.vtk_to_numpy(data.GetPointData().GetArray(0))
    dataset = dataset.reshape(dim, order='F')

    return dataset

if __name__ == '__main__':

    A = np.random.rand(3,3,3)

    writeNow(A, 'curvature.vtk')
    
    #B = np.random.rand(10,10,10,3)

    C = importTest('curvature.vtk')

    import pdb; pdb.set_trace()
    
