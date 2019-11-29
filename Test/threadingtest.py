from multiprocessing.pool import ThreadPool

import numpy as np

def thread(matrix):
    print("matrix:", matrix)
    return matrix * matrix

if __name__ == '__main__':

    data = np.random.rand(10,10,10)

    print("data:", data)

    pool = ThreadPool(10)

    result = pool.map(thread, data)

    pool.close()
    pool.join()

    print("result:", result)
