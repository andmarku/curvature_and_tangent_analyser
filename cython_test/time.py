import numpy as np
import cython_eigenFunction as cythonFcn
from definitionTester import testAgainstDefinition

def cython(matrices,nrOfTests):
    for k in range(0,nrOfTests):
        egVec = cythonFcn.calculateTangent(matrices[k,:,:])

def eighFcn(matrices,nrOfTests):
    for k in range(0,nrOfTests):
        eigs, vecs = np.linalg.eigh(matrices[k,:,:])
        index = np.argmin(abs(eigs))
        egVec = vecs[:, index]

def createMatrices(seedForRandom, nrOfTests):
    np.random.seed(seedForRandom)
    matrices = np.zeros((nrOfTests, 3, 3))
    for k in range(0,nrOfTests):
        matrix =  2 * (np.random.random_sample(9).reshape(3,3) - 0.5)
        matrices[k, : , :] = np.matmul(matrix, np.transpose(matrix))
    return matrices

def testFcns(matrices,nrOfTests):
    print("testing cython")
    cython(matrices,nrOfTests)

    print("testing eigh")
    eighFcn(matrices,nrOfTests)

if __name__ == '__main__':
    seedForRandom = 10
    nrOfTests = 200*200*2
    print("Running " + str(nrOfTests) + " iterations\n")

    print("create matrices")
    matrices = createMatrices(seedForRandom, nrOfTests)

    print("entering test module")
    testFcns(matrices,nrOfTests)
