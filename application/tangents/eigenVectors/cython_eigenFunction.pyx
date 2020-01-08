import Cython
from numpy import linalg as LA
import numpy as np
cimport numpy as cnp
from libc.math cimport sqrt
from libc.math cimport cos
from libc.math cimport acos
from libc.math cimport pow

# assumes that all-zero elements are taken care of before function
cpdef cnp.ndarray[double, ndim=1] calculateTangent(cnp.ndarray arg):

    # casting from numpy array
    cdef double[9] arg_as_array = [
       <double> arg[0][0], <double> arg[0][1], <double> arg[0][2] ,
       <double> arg[1][0], <double> arg[1][1], <double> arg[1][2] ,
       <double> arg[2][0], <double> arg[2][1], <double> arg[2][2]]

    # create the matrix (M - lambda I)
    cdef double smallestEgValue = calculateEigenValue(arg_as_array)

    # update matrix
    arg_as_array[0] = arg_as_array[0] - smallestEgValue
    arg_as_array[4] = arg_as_array[4] - smallestEgValue
    arg_as_array[8] = arg_as_array[8] - smallestEgValue

    # temporary printing
    #print("printing eigenvalue " + str(smallestEgValue))

    # the not yet normalized eigenvector
    cdef double[3] raw_egVec
    raw_egVec = calcEgVecByCrossProduct(arg_as_array, raw_egVec)

    # normalize
    cdef double[3] egVec = normalizeVector(raw_egVec)

    # cast to numpy array
    cdef cnp.ndarray[cnp.double_t, ndim=1] npEgVec = np.asarray(egVec)

    return npEgVec

# function for finding eigenvalues through cross products
# the method relies on that the input matrix is normal, which is fulfilled for
# symmetric matrices
cdef double* calcEgVecByCrossProduct(double[9] arg, double[3] egVec):
    # constant to protect from rounding of errors
    cdef double cutOffConstant = 0

    cdef double[3] v1 = [arg[0], arg[1], arg[2]]
    cdef double[3] v2 = [arg[3], arg[4], arg[5]]
    cdef double[3] v3 = [arg[6], arg[7], arg[8]]

    # -------- Case 1 (most likely) --------
    #   two indep. columns, geometric multiplicitiy: 1
    #   -> the column space has rank 2
    # idea:
    #   use two of the vectors spanning the column space to find the egVector
    #   by taking the cross product
    # implementation:
    #   take cross product of two random vectors.
    #   If the cross product is zero, they are parallell, which won't work. If so,
    #   try the next pair, and potentially the third.
    #   Then return the first (normalized) nonzero vector

    # returning any nonzero cross product
    # (also make sure that the vector only nonzero due to arithmetic faults)

    egVec = calcCross(v1,v2, egVec)
    if(calcDot(egVec, egVec) > cutOffConstant):
      return egVec
    egVec = calcCross(v1, v3, egVec)
    if(calcDot(egVec, egVec) > cutOffConstant):
      return egVec
    egVec = calcCross(v2,v3, egVec)
    if(calcDot(egVec, egVec) > cutOffConstant):
      return egVec

    # -------- Case 2 --------
    #   one independent columns = geometric multiplicitiy: 2
    #   -> all columns are either zero-vectors or on the same line. At least one
    #   vector is non-zero.
    #   -> cross product of any two vectors should be zero
    # idea:
    #   cross product between any non null column vector and any vector not
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

    cdef double[3] v_to_rotate
    cdef double[3] v_rotated
    cdef int isVectorNonZero = 0

    # find a vector that is nonzero
    if(calcDot(v1, v1) > cutOffConstant):
        v_to_rotate = v1
        isVectorNonZero = 1
    elif(calcDot(v2, v2) > cutOffConstant):
        v_to_rotate = v2
        isVectorNonZero = 1
    elif(calcDot(v3, v3) > cutOffConstant):
        v_to_rotate = v3
        isVectorNonZero = 1

    # create a new vector through rotating the nonzer vector and return the cross
    # product between the two
    cdef double norm_sqrd
    if(isVectorNonZero == 1):
        norm_sqrd = calcDot(v_to_rotate, v_to_rotate)
        v_rotated = rotateVector(v_to_rotate, v_rotated)
        egVec = calcCross(v_to_rotate, v_rotated,egVec)
        norm_sqrd = calcDot(egVec, egVec)
        return egVec

    # -------- Case 3 (least likely) --------
    #   all values are zero, geometric multiplicitiy: 3
    #   -> any nonzero vector will do, but this will be misleading. The zero
    #     vector is therefore returned
    #   -> it's also possible to end up here if all vectors where very small. In
    #     this case, returning the zero vector is also the most reasonable.
    egVec[0] = 0
    egVec[1] = 0
    egVec[2] = 0
    return egVec

# cdef double newCalculateEigenValue(double[9] my_matrix):
#     cdef double eig1
#     cdef double eig2
#     cdef double eig3
#     cdef double m_00_q
#     cdef double m_11_q
#     cdef double m_22_q
#     cdef double determinant
#     cdef double pi
#     cdef double phi
#
#     # all values are not needed since the matrix is symmetric
#     cdef double m_00 = my_matrix[0]
#     cdef double m_01 = my_matrix[1]
#     cdef double m_02 = my_matrix[2]
#     cdef double m_11 = my_matrix[4]
#     cdef double m_12 = my_matrix[5]
#     cdef double m_22 = my_matrix[8]
#
#     cdef double p1 = pow(m_01,2) + pow(m_02,2) + pow(m_12,2)
#     # if A is diagonal.
#     if (p1 == 0):
#       eig1 = m_00
#       eig2 = m_11
#       eig3 = m_22
#     else:
#       q = (m_00 + m_11 + m_22)/3               # 3q = trace(A) = the sum of all diagonal values
#       p2 = pow((m_00 - q),2) + pow((m_11 - q),2) + pow((m_22 - q),2) + 2 * p1
#       p = sqrt(p2 / 6)
#
#       # doing B = A - q * I    # I is the identity matrix
#       m_00_q = m_00 - q
#       m_11_q = m_11 - q
#       m_22_q = m_22 - q
#
#       # determinant of A - q * I
#       determinant = m_00_q * m_11_q * m_22_q + \
#       2 * (m_01 * m_12 * m_02) - \
#       m_00_q * (m_12 * m_12) - \
#       m_11_q * (m_02 * m_02) - \
#       m_22_q * (m_01 * m_01)
#
#       r = (3 / p) * determinant / 2
#
#       # In exact arithmetic for a symmetric matrix  -1 <= r <= 1
#       # but computation error can leave it slightly outside this range.
#       pi = 3.14159265358979323846
#       if (r <= -1):
#         phi = pi / 3
#       elif (r >= 1):
#         phi = 0
#       else:
#         phi = acos(r) / 3
#
#       # the eigenvalues satisfy eig3 <= eig2 <= eig1
#       eig1 = q + 2 * p * cos(phi)
#       eig3 = q + 2 * p * cos(phi + (2 * pi / 3))
#       eig2 = 3 * q - eig1 - eig3     # since trace(A) = eig1 + eig2 + eig3
#       print(str(eig1) + " and " + str(eig2) + " and " + str(eig3))
#
#     # find the eigenvalue with the smallest absolute value
#     cdef double smallestEgValue
#     if(eig1*eig1 < eig2*eig2):
#      if(eig1*eig1 < eig3*eig3):
#        # eig1^2 is smaller than both eig1^2 and eig2^3
#        smallestEgValue = eig1
#      else:
#        # eig3^2 is smaller than both eig1^2 and eig2^2
#        smallestEgValue = eig3
#     else:
#      if(eig2*eig2 < eig3*eig3):
#        # eig2^2 is smaller than both eig1^2 and eig3^2
#        smallestEgValue = eig2
#      else:
#        # eig3^2 is smaller than both eig1^2 and eig2^2
#        smallestEgValue = eig3
#     return smallestEgValue

# !!!! OBS!!!! only works for symmetrical matrices
# implemented from https://d1rkab7tlqy5f1.cloudfront.net/TNW/Over%20faculteit/
#                                   Decaan/Publications/1999/SCIA99GKNBLVea.pdf
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

    # make sure not to divide by zero or very close numbers
    small_constant = 0.000000000000001
    if(qSqrt < small_constant):
        print("qSqrt was too small " + str(qSqrt))
        print(m_00)
        print(m_01)
        print(m_02)
        print(m_11)
        print(m_12)
        print(m_22)
        qSqrt = small_constant

    # make sure that R / qSqrt does not step outside [-1,1] (may happen by arithmetic
    # rounding errors)
    cdef double r_qSrt = R / qSqrt
    if(r_qSrt < -1):
      r_qSrt = -1
    if(r_qSrt > 1):
      r_qSrt = 1

    # prep for formula
    cdef double theta = acos( r_qSrt )
    # cdef double PI = 3.14159265358979323846

    # formula for computing the eigenvalues
    cdef double eig1 = -2 * sqrt(Q) * cos( theta/3 ) - a / 3
    # cdef double eig2 = -2 * sqrt(Q) * cos( (theta + PI)/3 ) - a / 3
    # cdef double eig3 = -2 * sqrt(Q) * cos( (theta - PI)/3 ) - a / 3

    # print(str(eig1) + " and " + str(eig2) + " and " + str(eig3))
    # # find the eigenvalue with the smallest absolute value
    # cdef double smallestEgValue
    # if(eig1*eig1 < eig2*eig2):
    #   if(eig1*eig1 < eig3*eig3):
    #     # eig1^2 is smaller than both eig1^2 and eig2^3
    #     smallestEgValue = eig1
    #   else:
    #     # eig3^2 is smaller than both eig1^2 and eig2^2
    #     smallestEgValue = eig3
    # else:
    #   if(eig2*eig2 < eig3*eig3):
    #     # eig2^2 is smaller than both eig1^2 and eig3^2
    #     smallestEgValue = eig2
    #   else:
    #     # eig3^2 is smaller than both eig1^2 and eig2^2
    #     smallestEgValue = eig3

    return eig1

# # function for normalizing a 3*1 vector
cdef double* normalizeVector(double[3] vector):
    cdef double norm = sqrt(calcDot(vector, vector))
    # make sure not to divide by zero
    if(norm == 0):
      return vector
    vector[0] = vector[0]/norm
    vector[1] = vector[1]/norm
    vector[2] = vector[2]/norm
    return vector

# function for rotating a vector two times (using operation taken from
# standard rotational matrix described at eg wikipedia)
cdef inline double* rotateVector(double[3] v, double[3] v_rotated):
    #first rotation
    cdef double x = v[0]
    cdef double y = v[1] * 0.86 - v[0]/2
    cdef double z = v[1]/2 + v[0] * 0.86
    # second rotation
    v_rotated[0] = x * 0.86 - y/2
    v_rotated[1] = x/2 + y * 0.86
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
