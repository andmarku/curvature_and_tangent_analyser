import Cython
import numpy as np
cimport numpy as cnp

''' Calculates the knutsson mapping of a vector

Input is on the form:
    numpy array: Eigenvector = (3)

Output is on the form:
    numpy array: Knutsson = (9)
'''
cpdef cnp.ndarray[double, ndim=1]  knutMap(cnp.ndarray vec):
    # casting from numpy array
    cdef double[3] vec_C = [ <double> vec[0], <double> vec[1], <double> vec[2]]

    cdef double areAllZero= vec_C[0] * vec_C[0] + vec_C[1] * vec_C[1] + vec_C[2] * vec_C[2]
    if(areAllZero == 0):
      return np.array([0,0,0,0,0,0,0,0,0])

    cdef double[9] flattenedKnutMap
    flattenedKnutMap = flatOuterOfSameVector(vec_C,flattenedKnutMap)
    return np.asarray(flattenedKnutMap)

cdef double* flatOuterOfSameVector(double[3] v, double[9] res):
    res[0] = v[0] * v[0]
    res[1] = v[1] * v[0]
    res[2] = v[2] * v[0]
    res[3] = v[0] * v[1]
    res[4] = v[1] * v[1]
    res[5] = v[2] * v[1]
    res[6] = v[0] * v[2]
    res[7] = v[1] * v[2]
    res[8] = v[2] * v[2]
    return res
