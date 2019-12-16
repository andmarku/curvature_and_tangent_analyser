import numpy as np

''' Calculates the knutsson mapping of a vector

Input is on the form:
    numpy array: eigenvector = (3, 3)

Output is on the form:
    numpy array: knutMap = (9,1)
'''

def knutssonMapping(eigenvector):
    knutMap = np.outer(eigenvector,eigenvector)/np.linalg.norm(eigenvector)
    return knutMap.flatten()

# if __name__ == '__main__':
#     # input: eigenvector from GST
#     eigenvector = np.random.rand(3,1)
#     print(eigenvector)
#     print(knutssonMapping(eigenvector, True))
#     print(knutssonMapping(eigenvector, True).shape)
