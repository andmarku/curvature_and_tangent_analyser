import numpy as np
from vtk.util import numpy_support as VN
import vtk
from vtk import vtkStructuredPointsWriter

def writeNow(input):

    dimensions = input.shape

    array = VN.numpy_to_vtk(input.ravel(), deep=True, array_type=vtk.VTK_FLOAT)

    data = vtk.vtkPointData()
    data.AddArray(array)

    points = vtk.vtkStructuredPoints()
    points.SetFieldData(data)
    points.SetDimensions(dimensions)

    writer = vtkStructuredPointsWriter()

    writer.SetFileName('testwritefile.vtk')

    writer.SetInputData(points)
    writer.Write()

    #stream = writer.OpenVTKFile()

    import pdb; pdb.set_trace()

    #data.SetDimensions(dimensions)

    #stream.WritePoints(data)

    print(data)

    #import pdb; pdb.set_trace()


if __name__ == '__main__':

    A = np.random.rand(10,10,10)

    writeNow(A)
