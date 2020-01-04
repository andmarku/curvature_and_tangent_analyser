import numpy as np
from numpy import linalg as LA

def testWithKnownSolutions(myFcn,epsilon):

    # nrOfTestCasesSingleEigenvec = 4
    # for k in range(1, nrOfTestCasesSingleEigenvec + 1):
    #     matrix, trueSol, nameOfTest = whichTestCaseSingleEigenvec(k)
    #     mySol = myFcn(matrix)
    #     closeEnough = isItAlignedSingleEigenvec(mySol, trueSol, epsilon)
    #     prettyPrinting(mySol,trueSol, nameOfTest, closeEnough)

    nrOfTestCasesTwoEigenvecs = 1
    for k in range(1, nrOfTestCasesTwoEigenvecs + 1):
        matrix, sol1, sol2, nameOfTest = whichTestCaseTwoEigenvec(k)
        mySol = myFcn(matrix)
        closeEnough = isItAlignedTwoEigenvecs(mySol, sol1, sol2, epsilon)
        prettyPrinting(mySol, nameOfTest, closeEnough)


# returns 1 if all the vectors are closer than epsilon to each other, otherwise it returns 0
# assumes that neither vector is the zero vector
def isItAlignedSingleEigenvec(mySol, trueSol, epsilon):
    mySol = mySol / LA.norm(mySol)
    trueSol = trueSol / LA.norm(trueSol)
    degreeOfOverlap = np.absolute(np.dot(mySol, trueSol))
    if(degreeOfOverlap < 1 - epsilon):
        return 0
    return 1

# check if mysol is a linear combination of sol1 and sol2. If so, return true (1),
# else return false (0)
def isItAlignedTwoEigenvecs(mySol, sol1, sol2, epsilon):
    # make sure all vectors are normalized
    mySol = mySol / LA.norm(mySol)
    sol1 = sol1 / LA.norm(sol1)
    sol2 = sol2 / LA.norm(sol2)

    # remove any sol1 component from mySol
    projection = np.dot(mySol, sol1) * sol1
    mySol = np.subtract(mySol, projection)

    # remove any sol2 component from mySol
    projection = np.dot(mySol, sol2) * sol2
    mySol = np.subtract(mySol, projection)

    # if there mySol has components not linearly dependent on sol1 and sol2
    # and it is larger than epsilon, then return false (ie 0)
    if(LA.norm(mySol) > epsilon):
        return 0
    return 1

def prettyPrinting(mySol, nameOfTest, closeEnough):
    if(closeEnough==1):
        print("Success!")
    else:
        print("******")
        print("--- WRONG ANSWER! ---")
        print("Test: " + nameOfTest)
        print("My solution: " + str(mySol))
        print("******")

def whichTestCaseSingleEigenvec(value):
    print("\n" + "Test number " + str(value))
    if(value == 1):
        matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        trueSol = np.array([1,0,0])
        nameOfTest = "zero matrix"
    if(value == 2):
        matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        trueSol = np.array([-1,0,0])
        nameOfTest = "zero matrix"
    if(value == 3):
        matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        trueSol = np.array([1,0,0.01])
        nameOfTest = "zero matrix"
    if(value == 4):
        matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        trueSol = np.array([1,0,-0.2])
        nameOfTest = "zero matrix"
    return matrix, trueSol, nameOfTest

def whichTestCaseTwoEigenvec(value):
    print("\n" + "Test number " + str(value))
    if(value == 1):
        matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        sol1 = np.array([1,0,0])
        sol2 = np.array([0,1,0])
        nameOfTest = "zero matrix"
    return matrix, sol1, sol2, nameOfTest
