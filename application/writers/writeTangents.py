import numpy
import vtk

from vtk.util import numpy_support

''' Writes the tangents to a vtk file.

    matrix: numpy array of dimensions (N1, N2, N3, 3).
    filename: string of the filename including extension 'vtk'.

    Writes to file the tangents as a vtkStructuredPoints object.
    Can be read using a vtkStructuredPointsReader at a later stage.
'''
def writeTangents(matrix, filename):

    dim = (matrix.shape[0], matrix.shape[1], matrix.shape[2])

    flat = matrix.reshape(-1, matrix.shape[-1])

    array = numpy_support.numpy_to_vtk(flat, deep=True, array_type=vtk.VTK_FLOAT)
    array.SetName("tangents")

    points = vtk.vtkStructuredPoints()
    points.SetDimensions(dim)
    points.GetPointData().AddArray(array)

    writer = vtk.vtkStructuredPointsWriter()
    writer.SetFileTypeToBinary()
    writer.SetFileName(filename)
    writer.SetInputData(points)
    writer.Write()

# Test function
if __name__ == "__main__":

    A = numpy.random.rand(5,5,5,3)

    writeTangents(A, "tangentstest.vtk")

    reader = vtk.vtkStructuredPointsReader()
    reader.SetFileName("tangentstest.vtk")
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    data = reader.GetOutput()
    dim = data.GetDimensions()

    actualdimensions = (dim[0], dim[1], dim[2], 3)

    dataset = numpy_support.vtk_to_numpy(data.GetPointData().GetArray(0))
    dataset = dataset.reshape(actualdimensions, order='F')

    print("dataset:", dataset)
