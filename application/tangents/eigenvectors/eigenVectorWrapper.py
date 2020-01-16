from cythonCalculator import calculateWithCython

def calculateEigenVectors(GST):
    data = calculateWithCython(GST)
    return data
