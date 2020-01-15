import Cython
import numpy as np
cimport numpy as cnp
from libc.math cimport sqrt

cpdef double  calcCurvature(cnp.ndarray vec):
    # cast from numpy array
    cdef double[9] vec_C = \
    [<double> vec[0], <double> vec[1], <double> vec[2],
     <double> vec[3], <double> vec[4], <double> vec[5],
     <double> vec[6], <double> vec[7], <double> vec[8]]

    # take the dot product
    cdef double curvature = \
      vec_C[0] * vec_C[0] + \
      vec_C[1] * vec_C[1] + \
      vec_C[2] * vec_C[2] + \
      vec_C[3] * vec_C[3] + \
      vec_C[4] * vec_C[4] + \
      vec_C[6] * vec_C[6] + \
      vec_C[5] * vec_C[5] + \
      vec_C[7] * vec_C[7] + \
      vec_C[8] * vec_C[8]

    # divide norm by 2 (instead of dividing result by sqrt of 2)
    curvature = curvature / 2

    # take the square root
    curvature = sqrt(curvature)

    return curvature
