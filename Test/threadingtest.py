
# Multithreading pool function
from multiprocessing.pool import ThreadPool

# Multiprocessing pool function
from multiprocessing.pool import Pool

import multiprocessing as mlp

import numpy as np
import time

''' CPU lighter function '''
def light(matrix):
    result = matrix * matrix
    return result

''' CPU heavier function '''
def heavy(matrix):
    result = np.zeros(matrix.shape)
    for (i,j), a in np.ndenumerate(matrix):
        result[i,j] = a + i + j
    return result

if __name__ == '__main__':

    CPU_COUNT = mlp.cpu_count()

    data = np.random.rand(200,200,200)

    time0 = time.time()

    result = light(data)

    time1 = time.time()

    pool = ThreadPool(5)
    result = pool.map(light, data)
    pool.close()
    pool.join()

    time2 = time.time()

    pool = Pool(CPU_COUNT)
    result = pool.map(light, data)
    pool.close()
    pool.join()

    time3 = time.time()

    print("--- CPU light function ---")
    print("sequential time elapsed:", time1 - time0)
    print("threading time elapsed:", time2 - time1)
    print("processing time elapsed:", time3 - time2)

    time0 = time.time()

    result = light(data)

    time1 = time.time()

    pool = ThreadPool(5)
    result = pool.map(heavy, data)
    pool.close()
    pool.join()

    time2 = time.time()

    pool = Pool(CPU_COUNT)
    result = pool.map(heavy, data)
    pool.close()
    pool.join()

    time3 = time.time()

    print("--- CPU heavy function ---")
    print("sequential time elapsed:", time1 - time0)
    print("threading time elapsed:", time2 - time1)
    print("processing time elapsed:", time3 - time2)
