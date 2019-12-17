import numpy as np
import time
import timeit
import python_eigenVectorCalculator as orig
import cython_eigenFunction as new

def mycode(args):
    for j in range(1,10000):
        y = orig.calculateTangent(args)
    return y

def myCythonCode(args):
    for j in range(1,10000):
        y = new.calculateTangent(args)
    return y

# def measureTime(a, arg):
#     data = range(1,4)
#     start = time.clock()
#     pool=ThreadPool(processes = 2)
#     output= [pool.map(mycode, range(1,4))]
#     pool.close()
#     print(output)
#     # for value in range(1,200*200):
#     #     a(arg)
#     #     #u,v =a(arg)
#     #     #u_min = min(u)
#     elapsed = time.clock()
#     elapsed = elapsed - start
#     print("Time spent in (function name) is: " + str(elapsed))

def measureTime(arg):
    start = time.clock()
    mycode(arg)
    elapsed = time.clock()
    elapsed = elapsed - start
    print("Time spent in (function name) is: " + str(elapsed))

    start = time.clock()
    print("\n")
    myCythonCode(arg)
    print("\n")
    elapsed = time.clock()
    elapsed = elapsed - start
    print("Time spent in (function name) is: " + str(elapsed))


if __name__ == '__main__':
    myMatrix = np.array([[2, 5, -1], [5, 2, 1], [-1, 1, 0]])
    measureTime(myMatrix)
