import numpy as np

def knutssonMapping(eigenvector, flatten = False):
    knutMap = np.outer(eigenvector,eigenvector)/np.linalg.norm(eigenvector)
    if flatten == True:
        knutMap = knutMap.flatten()
    return knutMap

if __name__ == '__main__':
    # input: eigenvector from GST
    eigenvector = np.random.rand(3,1)
    print(eigenvector)
    print(knutssonMapping(eigenvector, True))
    print(knutssonMapping(eigenvector, True).shape)
