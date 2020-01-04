import numpy as np
import time
import timeit
import python_eigenVectorCalculator as orig
import cython_eigenFunction as new
import scipy.linalg as sp


def mycode(args, itr):
    for j in range(1,itr):
        y = orig.calculateTangent(args)
    return y

def myCythonCode(args, itr):
    for j in range(1,itr):
        y = new.calculateTangent(args)
    return y

def npEighFcn(args, itr):
    for j in range(1,itr):
        eigs, vecs = np.linalg.eigh(args)
        index = np.argmin(abs(eigs))
    return vecs[:,index]

def spEigFcn(args, itr):
    for j in range(1,itr):
        eigs, vecs = sp.eig(args)
        index = np.argmin(abs(eigs))
    return vecs[:,index]


def measureTime(arg):
    itr = 100000

    print("Calculating smallest eigenvalue and corresponding eigenvector " + str(itr) + " times each with various implementations")

    start = time.clock()
    mycode(arg, itr)
    elapsed = time.clock()
    elapsed = elapsed - start
    print("Time spent in my python eigen function is: " + str(elapsed))

    start = time.clock()
    print("\n")
    myCythonCode(arg, itr)
    elapsed = time.clock()
    elapsed = elapsed - start
    print("Time spent in my cython eigen function is: " + str(elapsed))

    start = time.clock()
    print("\n")
    npEighFcn(arg, itr)
    elapsed = time.clock()
    elapsed = elapsed - start
    print("Time spent in np.eigh is: " + str(elapsed))

    start = time.clock()
    print("\n")
    spEigFcn(arg, itr)
    elapsed = time.clock()
    elapsed = elapsed - start
    print("Time spent in sp.eig is: " + str(elapsed))


if __name__ == '__main__':
    myMatrix = np.array([[2, 5, -1], [5, 2, 1], [-1, 1, 0]])
    # new.calculateTangent(myMatrix)
    measureTime(myMatrix)
