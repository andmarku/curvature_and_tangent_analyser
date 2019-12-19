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
    
    dims = matrix.shape

    flat = matrix.ravel(order='F')

    vtkarray = numpy_support.numpy_to_vtk(flat, False, vtk.VTK_FLOAT)
    vtkarray.SetNumberOfComponents(3)
    vtkarray.SetName("tangents")

    imagedata = vtk.vtkImageData()
    imagedata.SetDimensions((dims[0], dims[1], dims[2]))
    imagedata.GetPointData().SetVectors(vtkarray)

    writer = vtk.vtkStructuredPointsWriter()
    writer.SetFileName(filename)
    writer.SetInputData(idata)
    writer.SetFileTypeToBinary()
    writer.Write()
