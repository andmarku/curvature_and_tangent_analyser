import numpy as np
import scipy.linalg as sp
from analysisWrapper import analyze

if __name__ == '__main__':
    # testing analyze
    tensor_tangents = np.zeros((10,10,10,3))
    tensor_curvatures = np.zeros((10,10,10))
    for x in range(10):
        for y in range(10):
            for z in range(10):
                a = np.random.randn()
                if(a > 0.6):
                    tensor_tangents[x,y,z,0] = np.random.randn()
                    tensor_tangents[x,y,z,1] = np.random.randn()
                    tensor_tangents[x,y,z,2] = np.random.randn()
                    tensor_curvatures[x,y,z] = a

    analyze(tensor_tangents, tensor_curvatures, 'test', 0)
