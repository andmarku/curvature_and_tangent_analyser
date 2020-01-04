import numpy as np
import python_eigenVectorCalculator as python
import cython_eigenFunction as cython
from knownSolutionTester import testWithKnownSolutions
from definitionTester import testAgainstDefinition
# python.calculateTangent(args)


if __name__ == '__main__':

    epsilon = 0.1

    # testWithKnownSolutions(cython.calculateTangent,epsilon)

    nrOfTests = 1000000
    # known problems:
        # - the line if(qSqrt * qSqrt < 0.0001) (line 177 in eigenfunction)
            # however, no trouble in a 1000000 itr test runt
        # - the line if(norm_sqrd > 0.001)
            # the cross products can actually become non-zero perhaps due to computational issues?

    testAgainstDefinition(cython.calculateTangent, nrOfTests, epsilon)

 #    matrix = np.array([[-0.06123829, -0.04217063, -0.07649207],
 # [-0.04217063,  0.19136441, -0.09280182],
 # [-0.07649207, -0.09280182, -0.16225783]])
 #
 #    res = np.linalg.eigh(matrix)
 #    print(res)
 #
 #    myRes = cython.calculateTangent(matrix)
 #    print(myRes)
