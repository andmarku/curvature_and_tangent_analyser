from eighCalculator import calculateWithEigh
from cythonCalculator import calculateWithCython

def calculateEigenVectors(GST):
    data = calculateWithEigh(GST)
    #data = calculateWithCython(GST)
    return data
