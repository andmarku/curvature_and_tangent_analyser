import numpy as np
import cython_eigenFunction as cython
from definitionTester import testAgainstDefinition

def testFcn(matrix):
    eigs, vecs = np.linalg.eigh(matrix)
    index = np.argmin(abs(eigs))
    return vecs[:, index]

if __name__ == '__main__':
    epsilon = 0.0000001
    nrOfTests = 100000
    print("Running " + str(nrOfTests) + " tests and checking with accuracy " + str(epsilon) + "\n")

    print("Cython function")
    testAgainstDefinition(cython.calculateTangent, nrOfTests, epsilon)
    print("Eigh function")
    testAgainstDefinition(testFcn, nrOfTests, epsilon)
