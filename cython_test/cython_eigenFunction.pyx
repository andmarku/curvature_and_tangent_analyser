import Cython
from numpy import linalg as LA
import numpy as np
cimport numpy as cnp
from libc.math cimport sqrt
from libc.math cimport cos
from libc.math cimport acos
from libc.math cimport pow

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!! OBS!!! is my indexing correct? do i pick out rows or columns??????????????????????
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# check for integer division

# assumes that all-zero elements are taken care of before function
#
# @cython.boundscheck(False) # turn off bounds-checking for entire function
# @cython.wraparound(False)  # turn off negative index wrapping for entire function
cpdef cnp.ndarray[double, ndim=1] calculateTangent(cnp.ndarray arg):

    # casting
    cdef double[9] arg_as_array = [
       <double> arg[0][0], <double> arg[0][1], <double> arg[0][2] ,
       <double> arg[1][0], <double> arg[1][1], <double> arg[1][2] ,
       <double> arg[2][0], <double> arg[2][1], <double> arg[2][2]]


    cdef double smallestEgValue = calculateEigenValue(arg_as_array)
    #print(smallestEgValue)
    arg_as_array[0] = arg_as_array[0] - smallestEgValue
    arg_as_array[4] = arg_as_array[4] - smallestEgValue
    arg_as_array[8] = arg_as_array[8] - smallestEgValue

    # the not yet normalized eigenvector
    cdef double[3] raw_egVec
    raw_egVec = calcEgVecByCrossProduct(arg_as_array, raw_egVec)
    #print(np.asarray(raw_egVec))
    cdef double[3] egVec = normalizeVector(raw_egVec)
    cdef cnp.ndarray[cnp.double_t, ndim=1] npEgVec = np.asarray(egVec)
    return npEgVec

# function for finding eigenvalues through cross products
# the method relies on that the input is normal, which is fulfilled for symmetric
# matrices
# @cython.boundscheck(False) # turn off bounds-checking for entire function
# @cython.wraparound(False)  # turn off negative index wrapping for entire function
cdef double* calcEgVecByCrossProduct(double[9] arg, double[3] egVec):
    cdef double[3] v1 = [arg[0], arg[1], arg[2]]
    cdef double[3] v2 = [arg[3], arg[4], arg[5]]
    cdef double[3] v3 = [arg[6], arg[7], arg[8]]

    # normalize the vectors to avoid round of troubles and such
    cdef double[3] normed_v1 = normalizeVector(v1)
    cdef double[3] normed_v2 = normalizeVector(v2)
    cdef double[3] normed_v3 = normalizeVector(v3)

    # initialize for later use
    cdef double norm_sqrd

    # case 1 (most likely): two indep. columns, eigenvalue multiplicitiy: 1
    #   -> the column space has rank 2
    # idea:
    #   use the two vectors spanning it to find the egVector using the cross product
    # implementation:
    #   take cross product of two random vectors. if it is zero, I'll try the next
    #   pair, and potentially the third. return the first (normalized) nonzero vector
    egVec = calcCross(normed_v1,normed_v2, egVec)
    norm_sqrd = calcDot(egVec, egVec)
    # make sure that the vector is not zero or only nonzero due to arithmetic faults
    if(norm_sqrd > 0.01):
      return egVec

    egVec = calcCross(normed_v1, normed_v3, egVec)
    norm_sqrd = calcDot(egVec, egVec)
    # make sure that the vector is not zero or only nonzero due to arithmetic faults
    if(norm_sqrd > 0.01):
      return egVec

    egVec = calcCross(normed_v2,normed_v3, egVec)
    norm_sqrd = calcDot(egVec, egVec)
    # make sure that the vector is not zero or only nonzero due to arithmetic faults
    if(norm_sqrd > 0.01):
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
    cdef double[3] v
    cdef double[3] v_rotated

    norm_sqrd = calcDot(normed_v1, normed_v1)
    if(norm_sqrd > 0.01):
        v = normed_v1
        v_rotated = rotateVector(v, v_rotated)
        egVec = calcCross(v, v_rotated,egVec)
        norm_sqrd = calcDot(egVec, egVec)
        if(norm_sqrd > 0.001):
            return egVec
    #print(4)
    #print(np.asarray(normed_v2))
    norm_sqrd = calcDot(normed_v2, normed_v2)
    if(norm_sqrd > 0.01):
        v = normed_v2
        v_rotated = rotateVector(v, v_rotated)
        egVec = calcCross(v, v_rotated,egVec)
        norm_sqrd = calcDot(egVec, egVec)
        if(norm_sqrd > 0.001):
            return egVec
    #print(5)
    norm_sqrd = calcDot(normed_v3, normed_v3)
    if(norm_sqrd > 0.01):
        v = normed_v3
        v_rotated = rotateVector(v, v_rotated)
        egVec = calcCross(v, v_rotated,egVec)
        norm_sqrd = calcDot(egVec, egVec)
        if(norm_sqrd > 0.001):
            return egVec

    # # case 3 (least likely): all values are zero, eigenvalue multiplicitiy: 3
    # #   -> any nonzero normalized vector will do
    # # idea:
    # # return [1, 0, 0]
    egVec[0] = 1
    egVec[1] = 0
    egVec[2] = 0
    return egVec


# !!!! OBS!!!! only works for symmetrical matrices
# implemented from https://d1rkab7tlqy5f1.cloudfront.net/TNW/Over%20faculteit/
#                                   Decaan/Publications/1999/SCIA99GKNBLVea.pdf
# @cython.boundscheck(False) # turn off bounds-checking for entire function
# @cython.wraparound(False)  # turn off negative index wrapping for entire function
cdef double calculateEigenValue(double[9] my_matrix):
    # all values are not needed since the matrix is symmetric
    cdef double m_00 = my_matrix[0]
    cdef double m_01 = my_matrix[1]
    cdef double m_02 = my_matrix[2]
    cdef double m_11 = my_matrix[4]
    cdef double m_12 = my_matrix[5]
    cdef double m_22 = my_matrix[8]

    # coefficents for characteristic equation
    cdef double a = -(m_00 + m_11 + m_22)
    cdef double b = m_00 * m_11 + m_00 * m_22 + m_11 * m_22 - \
    ( (m_01 * m_01) + (m_02 * m_02) + (m_12 * m_12) )
    cdef double c = m_22 * (m_01 * m_01) + m_11 * (m_02 * m_02) + \
    m_00 * (m_12 * m_12) -  \
    (m_00 * m_11 * m_22 + 2 * m_01 * m_02 * m_12)

    # prep for formula
    cdef double Q = (a * a - 3 * b)/9
    cdef double R = ( 2 * pow(a,3) - 9 * a * b + 27 * c ) / 54
    cdef double qSqrt =  sqrt( pow(Q,3) )

    if(qSqrt < 0.0001):
        print("qSqrt was too small")
        return 0

    cdef double arccosTerm = acos( R / qSqrt )

    # compute smallest eigenvalue
    cdef double egValue = -2 * sqrt(Q) * cos( arccosTerm/3 ) - a / 3

    return egValue

# # function for normalizing a 3*1 vector
# @cython.boundscheck(False) # turn off bounds-checking for entire function
# @cython.wraparound(False)  # turn off negative index wrapping for entire function
cdef double* normalizeVector(double[3] vector):

    cdef double norm = sqrt(calcDot(vector, vector))

    # make sure not to divide by zero
    if(norm == 0):
      return vector
    vector[0] = vector[0]/norm
    vector[1] = vector[1]/norm
    vector[2] = vector[2]/norm
    return vector



# function for rotating a vector
cdef inline double* rotateVector(double[3] v, double[3] v_rotated):
    x = v[0]
    y = v[1]
    z = v[2]
    #first rotation
    y = y * 0.86 - x/2
    z = y/2 + x * 0.86
    # second rotation
    x = x * 0.86 - y/2
    y = x/2 + y * 0.86

    v_rotated[0] = x
    v_rotated[1] = y
    v_rotated[2] = z
    return v_rotated

# function for calculating cross product of two 3x1 vectors
cdef inline double* calcCross(double[3] v1, double[3] v2, double[3] crossVec):
    crossVec[0] = v1[1] * v2[2] - v1[2] * v2[1]
    crossVec[1] = v1[2] * v2[0] - v1[0] * v2[2]
    crossVec[2] = v1[0] * v2[1] - v1[1] * v2[0]
    return crossVec

# function for calculating dot product between two 3x1 vectors
cdef inline double calcDot(double[3] v1, double[3] v2):
    cdef double prod = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
    return prod
