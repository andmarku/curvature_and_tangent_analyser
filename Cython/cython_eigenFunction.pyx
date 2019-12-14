import Cython
import numpy as np
import math
from numpy import linalg as LA
cimport numpy as np
from libc.math cimport sqrt
from libc.math cimport cos
from libc.math cimport acos
from libc.math cimport pow

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!! OBS!!! is my indexing correct? do i pick out rows or columns??????????????????????
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# check for integer division

# @cython.boundscheck(False) # turn of bounds-checking for entire function
cpdef np.ndarray[double, ndim=1] calculateTangent(np.ndarray[long, ndim=2] arg):
    if(not np.any(arg)):
        return arg[0][:]

    # casting
    cdef double[9] arg_as_array = [
       <double> arg[0][0], <double> arg[0][2], <double> arg[0][2] ,
       <double> arg[1][0], <double> arg[1][2], <double> arg[1][2] ,
       <double> arg[2][0], <double> arg[2][2], <double> arg[2][2]]

    cdef double smallestEgValue = calculateEigenValue(arg_as_array)
    # print(smallestEgValue)

    cdef double x = arg_as_array[0] - smallestEgValue
    cdef double y = arg_as_array[0] - smallestEgValue
    cdef double z = arg_as_array[0] - smallestEgValue
    cdef double[3] sendIn = [x,y,z]
    cdef np.ndarray[double, ndim=1] tangent = calcEgVecByCrossProduct(sendIn)
    tangent[0] = tangent[0] * smallestEgValue
    tangent[1] = tangent[1] * smallestEgValue
    tangent[2] = tangent[2] * smallestEgValue
    # print(tangent)

    return tangent

cdef np.ndarray[double, ndim=1] calcCross(double[3] v1, double[3] v2, np.ndarray[double, ndim=1] egVec):
    egVec[0] = v1[1] * v2[2] - v1[2] * v2[1]
    egVec[1] = v1[2] * v2[0] - v1[0] * v2[2]
    egVec[2] = v1[0] * v2[1] - v1[1] * v2[0]
    return egVec

cdef double calcDot(double[3] v1, double[3] v2):
    cdef double prod = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
    return prod

# @cython.boundscheck(False) # turn of bounds-checking for entire function
cdef np.ndarray[double, ndim=1] calcEgVecByCrossProduct(double[9] arg):
    cdef double[3] v1 = [arg[0], arg[1], arg[2]]
    cdef double[3] v2 = [arg[3], arg[4], arg[5]]
    cdef double[3] v3 = [arg[6], arg[7], arg[8]]

    # initialize return type
    cdef np.ndarray[double, ndim=1] egVec = np.zeros([3])

    # case 1 (most likely): two indep. columns, eigenvalue multiplicitiy: 1
    #   -> the column space has rank 2
    # idea:
    #   use the two vectors spanning it to find egVector the cross product
    # implementation:
    #   take cross product of two random vectors. if it is zero, I'll try the next
    #   pair, and potentially the third. return the first (normalized) nonzero vector
    cdef np.ndarray[double, ndim=1] cross1 = calcCross(v1,v2,egVec)
    if(np.any(cross1)):
        if(cross1.dot(cross1) > 0.0001):
            egVec = cross1/sqrt(cross1.dot(cross1))
            return egVec

    cdef np.ndarray[double, ndim=1] cross2 = calcCross(v1, v3,egVec)
    if(np.any(cross2)):
        if(cross2.dot(cross2) > 0.0001):
            egVec = cross2/sqrt(cross2.dot(cross2))
            return egVec

    cdef np.ndarray[double, ndim=1] cross3 = calcCross(v2,v3,egVec)
    if(np.any(cross3)):
        if(cross3.dot(cross3) > 0.0001):
            egVec = cross3/sqrt(cross3.dot(cross3))
            return egVec

    # case 2: one independent columns =  eigenvalue multiplicitiy: 2
    #   -> all columns are either null or on the same line with at least one
    #   vector is non-zero
    #   -> cross product of any two vectors should be zero
    # idea:
    #   cross product between any non null column vector and a vector not
    #   aligned to the line will give one possible egVector
    # implementation:
    #   generate new vector through rotating any nonzero column vector
    # (https://en.wikipedia.org/wiki/Rotation_matrix)
    # 30 degrees around x axis
    #   p_first = [1 0     0
    #             0  0.86 -1/2
    #             0  1/2   0.86]
    # 30 degrees around z axis
    #   p_sec = [ 0.86 -1/2 0
    #             1/2 0.86  0
    #             0    0    1]
    #   return the normalized cross produc
    cdef double x
    cdef double y
    cdef double z
    cdef double[3] v
    # if(np.any(v1)):
    #     v = v1
    #     x = v[0]
    #     y = v[1]
    #     z = v[2]
    #     #first rotation
    #     y = y * 0.86 - x/2
    #     z = y/2 + x * 0.86
    #     # second rotation
    #     x = x * 0.86 - y/2
    #     y = x/2 + y * 0.86
    #     egVec = calcCross(v, np.array([x,y,z]),egVec)
    #     if(egVec.dot(egVec) > 0.0001):
    #         return egVec/sqrt(egVec.dot(egVec))
    #
    # if(np.any(v2)):
    #     v = v2
    #     x = v[0]
    #     y = v[1]
    #     z = v[2]
    #     #first rotation
    #     y = y * 0.86 - x/2
    #     z = y/2 + x * 0.86
    #     # second rotation
    #     x = x * 0.86 - y/2
    #     y = x/2 + y * 0.86
    #     egVec = calcCross(v, np.array([x,y,z]),egVec)
    #     if(egVec.dot(egVec) > 0.0001):
    #         return egVec/sqrt(egVec.dot(egVec))
    #
    # if(np.any(v3)):
    #     v = v3
    #     x = v[0]
    #     y = v[1]
    #     z = v[2]
    #     #first rotation
    #     y = y * 0.86 - x/2
    #     z = y/2 + x * 0.86
    #     # second rotation
    #     x = x * 0.86 - y/2
    #     y = x/2 + y * 0.86
    #     egVec = calcCross(v, np.array([x,y,z]),egVec)
    #     if(egVec.dot(egVec) > 0.0001):
    #         return egVec/sqrt(egVec.dot(egVec))

    # case 3 (least likely): all values are zero, eigenvalue multiplicitiy: 3
    #   -> any nonzero normalized vector will do
    # idea:
    # return [1, 0, 0]
    egVec[0] = 1
    return egVec


# !!!! OBS!!!! only works for symmetrical matrices
# implemented from https://d1rkab7tlqy5f1.cloudfront.net/TNW/Over%20faculteit/
#                                   Decaan/Publications/1999/SCIA99GKNBLVea.pdf
# @cython.boundscheck(False) # turn of bounds-checking for entire function
cdef double calculateEigenValue(double[9] my_matrix):
    cdef double m_00 = my_matrix[0]
    cdef double m_01 = my_matrix[1]
    cdef double m_02 = my_matrix[2]
    # cdef double m_10 = my_matrix[3]
    cdef double m_11 = my_matrix[4]
    cdef double m_12 = my_matrix[5]
    # cdef double m_20 = my_matrix[6]
    # cdef double m_21 = my_matrix[7]
    cdef double m_22 = my_matrix[8]

    # coefficents for characteristic equation
    cdef double a = -(m_00 + m_11 + m_22)
    cdef double b = m_00 * m_11 + m_00 * m_22 + m_11 * m_22 - \
    ( (m_01 * m_01) + (m_02 * m_02) + (m_12 * m_12) )
    cdef double c = m_22 * (m_01 * m_01) + m_11 * (m_02 * m_02) + \
    m_00 * (m_12 * m_12) -  \
    (m_00 * m_11 * m_22 + 2 * m_01 * m_02 * m_12)

    # # coefficents for characteristic equation
    # cdef double a = -(my_matrix[0,0] + my_matrix[1,1] + my_matrix[2,2])
    # cdef double b = my_matrix[0,0] * my_matrix[1,1] + my_matrix[0,0] * my_matrix[2,2] + my_matrix[1,1] * my_matrix[2,2] - \
    # ( np.square(my_matrix[0,1]) + np.square(my_matrix[0,2]) + np.square(my_matrix[1,2]))
    # cdef double c = my_matrix[2,2] * np.square(my_matrix[0,1]) + my_matrix[1,1] * np.square(my_matrix[0,2]) + \
    # my_matrix[0,0] * np.square(my_matrix[1,2]) -  \
    # (my_matrix[0,0] * my_matrix[1,1] * my_matrix[2,2] + 2 * my_matrix[0,1] * my_matrix[0,2] * my_matrix[1,2])

    # prep for formula
    cdef double Q = (a * a - 3 * b)/9
    cdef double R = ( 2 * pow(a,3) - 9 * a * b + 27 * c ) / 54
    cdef double qSqrt =  sqrt( pow(Q,3) )

    if(qSqrt * qSqrt < 0.0001):
        return 0

    cdef double arccosTerm = acos( R / qSqrt )

    # compute smallest eigenvalue
    cdef double egValue = -2 * sqrt(Q) * cos( arccosTerm/3 ) - a / 3

    return egValue
