import numpy as np
import python_eigenVectorCalculator as python
import cython_eigenFunction as cython
from knownSolutionTester import testWithKnownSolutions
#from definitionTester import testAgainstDefinition
# python.calculateTangent(args)


if __name__ == '__main__':
    testWithKnownSolutions(cython.calculateTangent)
