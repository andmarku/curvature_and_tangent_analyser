import numpy
import vtk

from vtk.util import numpy_support

''' Writes the tangents to a vtk file.

    matrix: numpy array of dimensions (N1, N2, N3, 3).
    filename: string of the filename including extension 'vtk'.

    Writes to file the tangents as a vtkStructuredPoints object.
    Can be read using a vtkStructuredPointsReader at a later stage.
'''
def write(matrix, filename):
       
    dims = matrix.shape

    flat = matrix.reshape((dims[0]*dims[1]*dims[2], 3))

    vtkarray = numpy_support.numpy_to_vtk(flat, False, vtk.VTK_FLOAT)
    vtkarray.SetNumberOfComponents(3)
    vtkarray.SetName("tangents")

    imagedata = vtk.vtkImageData()
    imagedata.SetDimensions((dims[0], dims[1], dims[2]))
    imagedata.GetPointData().SetVectors(vtkarray)

    writer = vtk.vtkStructuredPointsWriter()
    writer.SetFileName(filename)
    writer.SetInputData(imagedata)
    writer.SetFileTypeToBinary()
    writer.Write()

''' Returns to the user matrix saved in vtk-file.

    filename: string of the filename including extension 'vtk'.

    Returns a matrix on the form (N1, N2, N3, 3) which was described
    in the vtk-file.
'''
def read(filename):

    reader = vtk.vtkStructuredPointsReader()
    reader.ReadAllScalarsOn()

    output = reader.GetOutput()
    dims = output.GetDimensions()

    matrix = numpy_support.vtk_to_numpy(output.GetPointData().GetArray(0))
    matrix = matrix.reshape((dims[0], dims[1], dims[2], 3), order='F')

    return matrix
