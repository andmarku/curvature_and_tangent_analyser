import sys
sys.path.append('./tangents/smoothing')
sys.path.append('./tangents/gst')
sys.path.append('./tangents/eigenvectors')
from GST0 import calculateGST0
from gaussianSmoothing import convolution
from eigenVectorWrapper import calculateEigenVectors

def tangents(d, fiber_width):
    partials = convolution(d, fiber_width)
    GST = calculateGST0(partials, fiber_width)
    tangents = calculateEigenVectors(GST)
    return tangents
