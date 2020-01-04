import numpy as np

def testWithKnownSolutions(myFcn):
    epsilon = 0.001
    nrOfTestCases = 4
    for k in range(1, nrOfTestCases+1):
        matrix, trueSol, nameOfTest = whichTestCase(k)
        mySol = myFcn(matrix)
        closeEnough = testIfAlmostAligned(mySol, trueSol, epsilon)
        prettyPrinting(mySol,trueSol, nameOfTest, closeEnough)

# returns 1 if mySol or the flipped mySol are close enough to trueSol
# else returns 0
def testIfAlmostAligned(mySol, trueSol, epsilon):
    orientation = 1
    if(isItCloseEnough(mySol, trueSol, epsilon, orientation) == 1):
        return 1

    orientation = -1
    if(isItCloseEnough(mySol, trueSol, epsilon, orientation) == 1):
        return 1
    return 0

# returns 1 if all the values are closer than epsilon to their corresponding
# true values, otherwise it returns 0
def isItCloseEnough(mySol, trueSol, epsilon, orientation):
    for i in range(0,3):
        proximity = np.absolute(orientation*mySol[i] - trueSol[i])
        # print("Proximity = " + str(proximity) + " for element " + str(i) + "with orientation " + str(orientation))
        if(proximity > epsilon):
            return 0
    return 1

def prettyPrinting(mySol,trueSol, nameOfTest, closeEnough):
    if(closeEnough==1):
        print("Success!")
    else:
        print("******")
        print("--- WRONG ANSWER! ---")
        print("Test: " + nameOfTest)
        print("My solution: " + str(mySol))
        print("True solution: " + str(trueSol))
        print("******")

def whichTestCase(value):
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
