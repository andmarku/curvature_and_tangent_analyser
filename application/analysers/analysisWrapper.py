import numpy as np
from curvatureHistogram import createCurvatureHistogram

def analyze(tensor_tangents, tensor_curvatures):
    createCurvatureHistogram(tensor_curvatures)
