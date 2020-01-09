import numpy as np
if __name__ == '__main__':
  knutMap = np.zeros(6)
  eigenvector = np.array([1,2,3])
  knutMap[0] = eigenvector[0]*eigenvector[0] - eigenvector[1]*eigenvector[1]
  knutMap[1] = 2*eigenvector[0]*eigenvector[1]
  knutMap[2] = 2*eigenvector[0]*eigenvector[2]
  knutMap[3] = 2*eigenvector[1]*eigenvector[2]
  knutMap[4] = eigenvector[1]*eigenvector[1] - eigenvector[2]*eigenvector[2]
  knutMap[5] = eigenvector[2]*eigenvector[2] - eigenvector[0]*eigenvector[0]
  knutMap = knutMap/np.linalg.norm(eigenvector)
  print(knutMap)
