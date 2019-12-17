import numpy as np
import scipy.linalg as sp

import sys
sys.path.append('./curvatures')
sys.path.append('./data')
sys.path.append('./reader')
sys.path.append('./tangents')
sys.path.append('./writers')
from vtkReader import readVTK
from tangentsWrapper import tangents
from curvatureWrapper import curvatures

def program(filename):
    d, x, y, z = readVTK(filename)
    print("finished reading in data")
    tensor_tangents = tangents(d)
    print("finished calculating tangents")
    tensor_curvatures = curvatures(tensor_tangents)
    print("finished calculating curvatures")
