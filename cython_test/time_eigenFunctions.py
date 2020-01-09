import numpy as np
import python_eigenVectorCalculator as python
import cython_eigenFunction as cython
from definitionTester import testAgainstDefinition

def cythonFcn(nrOfTests, seedForRandom):
    np.random.seed(seedForRandom)
    for k in range(0,nrOfTests):
        matrix =  2 * (np.random.random_sample(9).reshape(3,3) - 0.5)
        symmetricMatric = np.matmul(matrix, np.transpose(matrix))
        egVec = cython.calculateTangent(symmetricMatric)

def eighFcn(nrOfTests, seedForRandom):
    np.random.seed(seedForRandom)
    for k in range(0,nrOfTests):
        matrix =  2 * (np.random.random_sample(9).reshape(3,3) - 0.5)
        symmetricMatric = np.matmul(matrix, np.transpose(matrix))
        eigs, vecs = np.linalg.eigh(matrix)
        index = np.argmin(abs(eigs))
        egVec = vecs[:, index]

if __name__ == '__main__':
    seedForRandom = 10
    nrOfTests = 100000
    print("Running " + str(nrOfTests) + "\n")

    print("Cython function\n")
    cythonFcn(nrOfTests, seedForRandom)

    print("Eigh function\n")
    eighFcn(nrOfTests, seedForRandom)
