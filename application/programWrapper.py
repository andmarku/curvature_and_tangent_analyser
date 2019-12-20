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

def program(filename, fiber_width):
    d, x, y, z = readVTK(filename)
    print("finished reading in data")

    tensor_tangents = tangents(d)
    print("finished calculating tangents")

    tensor_curvatures = curvatures(tensor_tangents)
    print("finished calculating curvatures")

    analyze(tensor_tangents, tensor_curvatures, filename, fiber_width)
