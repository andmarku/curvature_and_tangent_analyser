import sys

import programWrapper

'''

Input parameters:
    filename: string for filename of vtk-file to read.
    fiber_width: user specified width of fiber (radius).
    curvature: curvature.txt file for true curvatures (can be omitted).

'''

if __name__ == '__main__':



    filename = str(sys.argv[1])
    fibrewidth = int(sys.argv[2])

    if len(sys.argv) == 4:
        curvature = sys.argv[3]
        programWrapper.program(filename, fibrewidth, curvature)
    else:
        programWrapper.program(filename, fibrewidth)
