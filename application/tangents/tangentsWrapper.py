import sys
sys.path.append('./tangents/smoothing')
sys.path.append('./tangents/gst')
sys.path.append('./tangents/eigenVectors')
from GST0 import calculateGST0
from gaussianSmoothing import convolution
from eigenVectorWrapper import calculateEigenVectors

def tangents(d, fiber_width):
    partials = convolution(d)
    GST = calculateGST0(partials, fiber_width)
    tangents = calculateEigenVectors(GST)
    return tangents
