import numpy as np
import cython_eigenFunction as cython
import cython_eigenFunction_2 as cython2
from definitionTester import testAgainstDefinition
import definitionTester2

def testFcn(matrix):
    eigs, vecs = np.linalg.eigh(matrix)
    index = np.argmin(abs(eigs))
    return vecs[:, index]

if __name__ == '__main__':
    epsilon = 0.0000001
    nrOfTests = 100
    print("Running " + str(nrOfTests*nrOfTests*nrOfTests) + " tests and checking with accuracy " + str(epsilon) + "\n")
    #
    # print("Cython function")
    # testAgainstDefinition(cython.calculateTangent, nrOfTests, epsilon)

    print("Cython function")
    definitionTester2.testAgainstDefinition(cython2.calculateTangent, nrOfTests, epsilon)
    #
    # print("Eigh function")
    # testAgainstDefinition(testFcn, nrOfTests, epsilon)
