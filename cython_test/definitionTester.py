import numpy as np
from numpy import linalg as LA

def testAgainstDefinition(myFun, nrOfTests, epsilon):
    np.random.seed(10)

    nrOfFailedTests = 0
    for k in range(0,nrOfTests):
        # Old version of test matrix
        # u =  2 * (np.random.random_sample(9).reshape(3,3) - 0.5)
        # symmetricMatric = u + np.transpose(u)

        # matrix =  2 * (np.random.random_sample(9).reshape(3,3) - 0.5)
        # symmetricMatric = np.matmul(matrix, np.transpose(matrix))
        #
        # create vector with uniformly random values in [-1.0, 1.0)
        u =  2 * (np.random.random_sample(3) - 0.5)
        # simulate a gradient structure tensor using the random vector
        symmetricMatric = np.outer(u, u)

        # use function to calculate egVector
        egVec = myFun(symmetricMatric)

        # use first part of definition
        matrixMultEgVec = np.matmul(symmetricMatric, egVec)

        # check for zero vectors
        if(not np.any(egVec)):
            # print("\nFailed with itr " + str(k) + " with matrix " + str(symmetricMatric))
            print("egVec was returned as zero vector!!")
            nrOfFailedTests = nrOfFailedTests + 1
            continue
        elif(not np.any(matrixMultEgVec)):
            # print("\nFailed with itr " + str(k) + " with matrix " + str(symmetricMatric))
            print("Matrix multiplied with egVec created zero vector!")
            nrOfFailedTests = nrOfFailedTests + 1
            continue

        # normalize
        egVec = egVec / LA.norm(egVec)
        matrixMultEgVec = matrixMultEgVec / LA.norm(matrixMultEgVec)

        # check how close the vectors are aligned
        # (the dot product is maximally positve or negative, when the two vectors
        # are wither aligned or opposite)
        discrepancy =  1 - np.absolute(matrixMultEgVec.dot(egVec))
        if(discrepancy > epsilon):
            # print("\nFailed with itr " + str(k) + " with matrix \n" + str(symmetricMatric))
            # print("The eigenvector was " + str(egVec))
            # print("Matrix mutipl. gave " + str(matrixMultEgVec))
            # print("The degree of discrepancy is " + str(discrepancy))
            nrOfFailedTests = nrOfFailedTests + 1
    if(nrOfFailedTests == 0):
        testGrade = "passed all tests"
    else:
        testGrade = "failed " + str(nrOfFailedTests) + " tests"
    print("The function " + testGrade + " out of " + str(nrOfTests) + " tests")
