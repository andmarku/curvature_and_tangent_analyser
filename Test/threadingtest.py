
# Multithreading pool function
from multiprocessing.pool import ThreadPool

# Multiprocessing pool function
from multiprocessing.pool import Pool

import numpy as np
import time

''' CPU lighter function '''
def light(matrix):
    result = matrix * matrix
    return result

''' CPU heavier function '''
def heavy(matrix):
    result = np.zeros(matrix.shape)
    for (i,j), m in np.ndenumerate(matrix):
        result[i,j] = m + i + j
    return result

if __name__ == '__main__':

    data = np.random.rand(100,100,100)

    time1 = time.time()

    pool = ThreadPool(5)
    result = pool.map(light, data)
    pool.close()
    pool.join()

    time2 = time.time()

    pool = Pool(5)
    result = pool.map(light, data)
    pool.close()
    pool.join()

    time3 = time.time()

    print("--- CPU light function ---")
    print("threading time elapsed:", time2 - time1)
    print("processing time elapsed:", time3 - time2)

    time1 = time.time()

    pool = ThreadPool(5)
    result = pool.map(heavy, data)
    pool.close()
    pool.join()

    time2 = time.time()

    pool = Pool(5)
    result = pool.map(heavy, data)
    pool.close()
    pool.join()

    time3 = time.time()

    print("--- CPU heavy function ---")
    print("threading time elapsed:", time2 - time1)
    print("processing time elapsed:", time3 - time2)
