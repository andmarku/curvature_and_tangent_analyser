import numpy as np
import cython_eigenFunction as cythonFcn
import cython_eigenFunction_2 as cythonFcn2
from definitionTester import testAgainstDefinition

def cython(matrices):
    data = np.zeros((matrices.shape[0], matrices.shape[1], matrices.shape[2], 3))
    for (i, j, k), m in np.ndenumerate(matrices[:,:,:,0,0]):
        data[i,j,k,:] = cythonFcn.calculateTangent(matrices[i,j,k,:,:])


def cython2(matrices):
    cythonFcn2.calculateTangent(matrices)


# def eighFcn(matrices,nrOfTests):
    # for k in range(0,nrOfTests):
    #     eigs, vecs = np.linalg.eigh(matrices[k,:,:])
    #     index = np.argmin(abs(eigs))
    #     egVec = vecs[:, index]

# def createMatrices(seedForRandom, nrOfTests):
#     np.random.seed(seedForRandom)
#     matrices = np.zeros((nrOfTests, 3, 3))
#     for k in range(0,nrOfTests):
#         matrix =  2 * (np.random.random_sample(9).reshape(3,3) - 0.5)
#         matrices[k, : , :] = np.matmul(matrix, np.transpose(matrix))
#     return matrices


def createMatrices(seedForRandom, nrOfTests):
    np.random.seed(seedForRandom)
    matrices = np.zeros((nrOfTests,nrOfTests,nrOfTests, 3, 3))
    for x in range(0,nrOfTests):
        for y in range(0,nrOfTests):
            for z in range(0,nrOfTests):
                matrix =  2 * (np.random.random_sample(9).reshape(3,3) - 0.5)
                matrices[x,y,z, : , :] = np.matmul(matrix, np.transpose(matrix))
    return matrices

def testFcns(matrices,nrOfTests):
    print("testing cython")
    cython(matrices)

    print("testing 2")
    cython2(matrices)

    # print("testing eigh")
    # eighFcn(matrices,nrOfTests)

if __name__ == '__main__':
    seedForRandom = 10
    nrOfTests = 50
    print("Running " + str(nrOfTests) + " iterations\n")

    print("create matrices")
    matrices = createMatrices(seedForRandom, nrOfTests)

    print(matrices.shape)
    print("entering test module")
    testFcns(matrices,nrOfTests)
