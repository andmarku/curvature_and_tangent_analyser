import numpy as np

# define constant
CONST_SQRT_OF_TWO = np.sqrt(2)

# calculate curvature using a knutsson mapped vector
def curvatureCalculator(knutVector):
    return CONST_SQRT_OF_TWO*np.linalg.norm(knutVector)
