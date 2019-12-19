import numpy
import vtk

from vtk.util import numpy_support

''' Writes the curvatures to a vtk file.

    matrix: numpy array of dimensions (N1, N2, N3).
    filename: string of the filename including extension 'vtk'.

    Writes to file the curvature as a vtkStructuredPoints object.
    Can be read using a vtkStructuredPointsReader at a later stage.
'''
def writeCurvatures(matrix, filename):

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
