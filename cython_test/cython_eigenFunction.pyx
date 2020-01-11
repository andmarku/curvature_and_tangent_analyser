import Cython
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
    cdef double smallestEgValue = calculateEigenValue(arg_as_array, arg)

    # update matrix
    arg_as_array[0] = arg_as_array[0] - smallestEgValue
    arg_as_array[4] = arg_as_array[4] - smallestEgValue
    arg_as_array[8] = arg_as_array[8] - smallestEgValue


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
    #   Then return the first nonzero vector

    # constant to protect from rounding of errors
    cdef double cutOffConstant = 1e-15

    # prep
    cdef double[3] v1 = [arg[0], arg[1], arg[2]]
    cdef double[3] v2 = [arg[3], arg[4], arg[5]]
    cdef double[3] v3 = [arg[6], arg[7], arg[8]]

    # return any nonzero orthogonal vector
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

    # -------- Case 2 & 3 --------
    #   one independent columns = geometric multiplicitiy: 2
    #   zero independent columns = geometric multiplicitiy: 3
    #   in this case, return the zero vector since there is no
    #   tangent. It would therefore be misleading to return an
    #   eigenvector corresponding to the eigenvalue.
    egVec[0] = 0
    egVec[1] = 0
    egVec[2] = 0
    return egVec

# !!!! OBS!!!! only works for symmetrical matrices
# implemented from https://d1rkab7tlqy5f1.cloudfront.net/TNW/Over%20faculteit/
#                                   Decaan/Publications/1999/SCIA99GKNBLVea.pdf
cdef double calculateEigenValue(double[9] my_matrix, cnp.ndarray arg):
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

    # make sure not to divide by zero
    if(qSqrt == 0):
        eigs, vecs = np.linalg.eigh(arg)
        minEgValue = np.argmin(abs(eigs))
        return  <double> minEgValue

    # make sure that R / qSqrt does not step outside [-1,1] (may happen by arithmetic
    # rounding errors)
    cdef double r_qSrt = R / qSqrt
    if(r_qSrt < -1):
      r_qSrt = -1
    if(r_qSrt > 1):
      r_qSrt = 1

    # prep for formula
    cdef double theta = acos( r_qSrt )
    cdef double PI = 3.14159265358979323846

    # formula for computing the eigenvalues
    cdef double eig1 = -2 * sqrt(Q) * cos( theta/3 ) - a / 3
    cdef double eig2 = -2 * sqrt(Q) * cos( (theta + 2 * PI)/3 ) - a / 3
    cdef double eig3 = -2 * sqrt(Q) * cos( (theta - 2 * PI)/3 ) - a / 3

    # find the eigenvalue with the smallest absolute value
    # (eig1 <= eig3 <= eig2 but have not found a reliable source on that eig1
    # is always positive)
    cdef double smallestEgValue
    if(eig1*eig1 < eig2*eig2):
      if(eig1*eig1 < eig3*eig3):
        # eig1^2 is smaller than both eig1^2 and eig2^3
        smallestEgValue = eig1
      else:
        # eig3^2 is smaller than both eig1^2 and eig2^2
        smallestEgValue = eig3
    else:
      if(eig2*eig2 < eig3*eig3):
        # eig2^2 is smaller than both eig1^2 and eig3^2
        smallestEgValue = eig2
      else:
        # eig3^2 is smaller than both eig1^2 and eig2^2
        smallestEgValue = eig3

    return smallestEgValue

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
