import numpy as np
import python_eigenVectorCalculator as python
import cython_eigenFunction as cython
from knownSolutionTester import testWithKnownSolutions
from definitionTester import testAgainstDefinition
from numpy import linalg as LA
import scipy.linalg as sp
from numpy.linalg import matrix_rank

def testFcn(matrix):
    eigs, vecs = np.linalg.eigh(matrix)
    index = np.argmin(abs(eigs))
    print("eigs " + str(eigs))
    print("choosen vec " + str(vecs[:, index]))
    return vecs[:, index]

if __name__ == '__main__':

    epsilon = 0.1

    # testWithKnownSolutions(cython.calculateTangent,epsilon)

    nrOfTests = 3

    #testAgainstDefinition(cython.calculateTangent, nrOfTests, epsilon)
    #testAgainstDefinition(testFcn, nrOfTests, epsilon)

    v1 = np.array([2.47613488e-01, -1.48584454e-03, -2.73886652e-01])
    v2 = np.array([-1.48584454e-03,  8.91604906e-06,  1.64350089e-03])
    v3 = np.array([-2.73886652e-01,  1.64350089e-03,  3.02947545e-01])

    eigV = np.array([0.17904652, 0.84579384, 0.50256853])

    matrix = np.array([[2.47613488e-01, -1.48584454e-03, -2.73886652e-01],
    [-1.48584454e-03,  8.91604906e-06,  1.64350089e-03],
    [-2.73886652e-01,  1.64350089e-03,  3.02947545e-01]])

    print("printing rank before " + str(matrix_rank(matrix)))

    cython.calculateTangent(matrix)

    egV = -1.438371366457858e-09
    matrix[0][0] = matrix[0][0] - egV
    matrix[1][1] = matrix[1][1] - egV
    matrix[2][2] = matrix[2][2] - egV
    print("printing rank after, back in python " + str(matrix_rank(matrix)) + "\n")

    print(np.cross(eigV, v1))
    print(np.cross(eigV, v2))
    print(np.cross(eigV, v3))

    print(eigV.dot(v1))
    print(eigV.dot(v2))
    print(eigV.dot(v3))

    print(np.cross(v1, v2))
    print(np.cross(v3, v2))
    print(np.cross(v1, v3))


 #    matrix = np.array([[ 0.89166442, -0.34127662, -0.82292891],
 # [-0.34127662,  0.13062058,  0.31496871],
 # [-0.82292891,  0.31496871, 0.75949199]])
 #    np.random.seed(12)
 #    for k in range(0,1):
 #        u =  2 * (np.random.random_sample(3) ) #- 0.5)
 #
 #        # simulate a gradient structure tensor using the random vector
 #        matrix = np.outer(u, u)
 #        print("\ninput matrix = \n" + str(matrix) + "\n")
 #
 #        eigs, vecs = sp.eig(matrix)
 #        index = np.argmin(abs(eigs))
 #        print("sp.eig")
 #        print("eigs " + str(eigs))
 #        print("choosen egV " + str(eigs[index]))
 #        print("choosen vec " + str(vecs[:, index]) + "\n")
 #
 #        eigs, vecs = np.linalg.eigh(matrix)
 #        index = np.argmin(abs(eigs))
 #        print("numpy.linalg.eigh")
 #        print("eigs " + str(eigs))
 #        print("choosen egV " + str(eigs[index]))
 #        print("choosen vec " + str(vecs[:, index]) + "\n")
 #
 #        print("cython implementation")
 #        myRes = cython.calculateTangent(matrix)
 #        print("my result " + str(myRes) + "\n")
