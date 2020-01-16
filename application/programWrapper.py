import numpy as np
import scipy.linalg as sp

import sys
sys.path.append('./testAnalysers')
sys.path.append('./curvatures')
sys.path.append('./inputData')
sys.path.append('./reader')
sys.path.append('./tangents')
sys.path.append('./writers')
from vtkReader import readVTK
from tangentsWrapper import tangents
from curvatureWrapper import curvatures
from analysisWrapper import analyze
from writeCurvatures import write as curvwrite
from writeTangents import write as tangwrite
from filterCurvatures import filterSmoothedCurvatures

def program(filename, fiber_width, curvature=''):
    d, x, y, z = readVTK(filename)
    print("finished reading in data")

    tensor_tangents = tangents(d, fiber_width)
    print("finished calculating tangents")

    tensor_curvatures = curvatures(tensor_tangents)
    print("finished calculating curvatures")

    nzCurvatures, nzTangents = filterSmoothedCurvatures(tensor_curvatures, tensor_tangents,x,y,z)
    print("finished filtering curvatures and tangents")

    # analyze(nzTangents, nzCurvatures, filename, fiber_width, curvature)
    # print("finished analysis")

    tangwrite(nzTangents, 'tangents.vtk')
    print("finished writing tangents to file")

    curvwrite(nzCurvatures, 'curvatures.vtk')
    print("finished writing curvatures to file")
