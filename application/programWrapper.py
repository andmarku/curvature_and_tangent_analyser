import numpy as np
import scipy.linalg as sp

import sys
sys.path.append('./analysers')
sys.path.append('./curvatures')
sys.path.append('./data')
sys.path.append('./reader')
sys.path.append('./tangents')
sys.path.append('./writers')
from vtkReader import readVTK
from tangentsWrapper import tangents
from curvatureWrapper import curvatures
from analysisWrapper import analyze
from writeCurvatures import write as curvwrite
from writeTangents import write as tangwrite

def program(filename, fiber_width, curvature=''):
    d, x, y, z = readVTK(filename)
    print("finished reading in data")

    tensor_tangents = tangents(d, fiber_width)
    print("finished calculating tangents")
    #import pdb; pdb.set_trace() 
    tensor_curvatures = curvatures(tensor_tangents)
    print("finished calculating curvatures")

    analyze(tensor_tangents, tensor_curvatures, filename, fiber_width, curvature)
    print("finished analysis")

    tangwrite(tensor_tangents, 'tangents.vtk')
    print("finished writing tangents to file")

    curvwrite(tensor_curvatures, 'curvatures.vtk')
    print("finished writing curvatures to file")
