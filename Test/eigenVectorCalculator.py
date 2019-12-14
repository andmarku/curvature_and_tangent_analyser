import numpy as np
import math
import time
from scipy.linalg import null_space
from numpy import linalg as LA

def calculateTangent(arg):
    smallestEgValue = calculateEigenValue(arg)
    tangent = calcEgVecByCrossProduct( arg - smallestEgValue*np.identity(3))
    tangent = tangent * smallestEgValue
    return tangent

def calcEgVecByCrossProduct(arg):
    # case 1 (most likely): two indep. columns, eigenvalue multiplicitiy: 1
    #   -> the column space has rank 2
    # idea:
    #   use the two vectors spanning it to find egVector the cross product
    # implementation:
    #   take cross product of two random vectors. if it is zero, I'll try the next
    #   pair, and potentially the third. return the first (normalized) nonzero vector
    cross1 = np.cross(arg[:,0], arg[:,1])
    if(np.any(cross1)):
        return cross1/np.sqrt(cross1.dot(cross1))

    cross2 = np.cross(arg[:,0], arg[:,2])
    if(np.any(cross2)):
        return cross2/np.sqrt(cross2.dot(cross2))

    cross3 = np.cross(arg[:,1], arg[:,2])
    if(np.any(cross3)):
        return cross3/np.sqrt(cross3.dot(cross3))

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
    #   return the normalized cross product
    if(np.any(arg[:,0])):
        x = arg[0,0]
        y = arg[1,0]
        z = arg[2,0]
        #first rotation
        y = y*0.86 - x/2
        z = y/2 + x*0.86
        # second rotation
        x = x*0.86 - y/2
        y = x/2 + y*0.86
        egVec = np.cross(arg[:,0], np.array([x,y,z]))
        return egVec/np.sqrt(egVec.dot(egVec))

    if(np.any(arg[:,1])):
        x = arg[0,1]
        y = arg[1,1]
        z = arg[2,1]
        #first rotation
        y = y*0.86 - x/2
        z = y/2 + x*0.86
        # second rotation
        x = x*0.86 - y/2
        y = x/2 + y*0.86
        egVec = np.cross(arg[:,1], np.array([x,y,z]))
        return egVec/np.sqrt(egVec.dot(egVec))

    if(np.any(arg[:,2])):
        x = arg[0,2]
        y = arg[1,2]
        z = arg[2,2]
        #first rotation
        y = y*0.86 - x/2
        z = y/2 + x*0.86
        # second rotation
        x = x*0.86 - y/2
        y = x/2 + y*0.86
        egVec = np.cross(arg[:,2], np.array([x,y,z]))
        return egVec/np.sqrt(egVec.dot(egVec))


    # case 3 (least likely): all values are zero, eigenvalue multiplicitiy: 3
    #   -> any nonzero normalized vector will do
    # idea:
    # return [1, 0, 0]
    return np.array([1, 0 ,0])


    # # old solution
    # c1 = arg[:,0]
    # c2 = arg[:,1]
    # c3 = arg[:,2]
    # c0_abs = math.sqrt(arg[:,0].dot(arg[:,0]))
    # c1_abs = math.sqrt(arg[:,1].dot(arg[:,1]))
    # c2_abs = math.sqrt(arg[:,2].dot(arg[:,2]))
    #
    # # check if any is zero then use other case
    # x = arg[:,0]
    # x_abs = c0_abs
    #
    # y = arg[:,1] - (arg[:,1].dot(arg[:,0]))*arg[:,1]/c1_abs
    # y_abs = math.sqrt(y.dot(y))
    # # check if y_abs is zero, then use other case
    #
    # z = arg[:,2] - (arg[:,2].dot(arg[:,0]))*arg[:,2]/c2_abs - \
    # arg[:,2].dot(y)*arg[:,2]/c2_abs
    # z_abs = math.sqrt(z.dot(z))
    #
    # if(z_abs < x_abs):
    #     if(z_abs < y_abs):
    #         egVec = np.cross(c1,c2)
    #     else:
    #         egVec = np.cross(c1,c3)
    # else:
    #     if(x_abs < y_abs):
    #         egVec = np.cross(c3,c2)
    #     else:
    #         egVec = np.cross(c3,c1)

# !!!! OBS!!!! only works for symmetrical matrices
# implemented from https://d1rkab7tlqy5f1.cloudfront.net/TNW/Over%20faculteit/
#                                   Decaan/Publications/1999/SCIA99GKNBLVea.pdf
def calculateEigenValue(arg):
    # coefficents for characteristic equation
    a = -(arg[0,0] + arg[1,1] + arg[2,2])
    b = arg[0,0]*arg[1,1] + arg[0,0]*arg[2,2] + arg[1,1]*arg[2,2] - \
    ( np.square(arg[0,1]) + np.square(arg[0,2]) + np.square(arg[1,2]))
    c = arg[2,2]*np.square(arg[0,1]) + arg[1,1]*np.square(arg[0,2]) + \
    arg[0,0]*np.square(arg[1,2]) -  \
    (arg[0,0]*arg[1,1]*arg[2,2] + 2*arg[0,1]*arg[0,2]*arg[1,2])

    # prep for formula
    Q = (np.square(a) - 3*b)/9

    R = ( 2 * np.power(a,3) - 9*a*b + 27*c ) / 54
    qSqrt =  math.sqrt( np.power( Q , 3 ) )
    arccosTerm = math.acos( R / qSqrt )

    # compute smallest eigenvalue
    egValue = -2 * math.sqrt(Q) * math.cos( arccosTerm/3 ) - a / 3

    return c

def measureTime(a, arg):
    start = time.clock()
    for value in range(1,200*200):
        a(arg)
        #u,v =a(arg)
        #u_min = min(u)
    elapsed = time.clock()
    elapsed = elapsed - start
    print("Time spent in (function name) is: " + str(elapsed))


# comment: my fcn can be simplified more, but probably not enough to bother,
# unless it's something dramatic
myMatrix = np.array([[2, 5, -1], [5, 2, 1], [-1, 1, 0]])
measureTime(calculateTangent, myMatrix)
measureTime( LA.eig, myMatrix)
