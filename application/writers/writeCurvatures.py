import numpy
import vtk

from vtk.util import numpy_support

''' Writes the curvatures to a vtk file.

    matrix: numpy array of dimensions (N1, N2, N3).
    filename: string of the filename including extension 'vtk'.

    Writes to file the curvature as a vtkStructuredPoints object.
    Can be read using a vtkStructuredPointsReader at a later stage.
'''
def write(matrix, filename):

    dims = matrix.shape

    flat = matrix.ravel(order='F')

    vtkarray = numpy_support.numpy_to_vtk(flat, deep=True, array_type=vtk.VTK_FLOAT)
    vtkarray.SetName("curvatures")

    points = vtk.vtkStructuredPoints()
    points.SetDimensions(dims)
    points.GetPointData().AddArray(vtkarray)

    writer = vtk.vtkStructuredPointsWriter()
    writer.SetFileTypeToBinary()
    writer.SetFileName(filename)
    writer.SetInputData(points)
    writer.Write()

''' Returns to the user matrix saved in vtk-file.

    filename: string of the filename including extension 'vtk'.

    Returns a matrix on the form (N1, N2, N3) which was described
    in the vtk-file.
'''
def read(filename):

    reader = vtk.vtkStructuredPointsReader()
    reader.ReadAllScalarsOn()

    output = reader.GetOutput()
    dims = output.GetDimensions()

    matrix = numpy_support.vtk_to_numpy(output.GetPointData().GetArray(0))
    matrix = matrix.reshape(dims, order='F')

    return matrix
