import sys
sys.path.append('./tangents/smoothing')
sys.path.append('./tangents/gst')
sys.path.append('./tangents/eigenVectors')
from GST0 import calculateGST0
from gaussianSmoothing import convolution
from eigenVectorWrapper import calculateEigenVectors

def tangents(d):
    partials = convolution(d)
    GST = calculateGST0(partials, 1)
    tangents = calculateEigenVectors(GST)
    return tangents
