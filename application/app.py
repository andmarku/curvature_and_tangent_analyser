import sys

import programWrapper

if __name__ == '__main__':

    filename = str(sys.argv[1])
    fibrewidth = int(sys.argv[2])

    programWrapper.program(filename, fibrewidth)
