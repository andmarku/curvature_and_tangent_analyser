Created by Elias Hölén Hannouch, Mikael Lennefors, and Markus Fällman.

Running the program
---
The program is in the folder 'application', with the 'app.py' file as the main file.

Before running the program, the Cython code must be compiled. This has to be done in
both the folder 'application\\curvature' and in the folder 'application\\tangents\\eigenvectors'.
To compile, run the following command in the terminal: python setup.py build_ext --inplace .
If you want to compile the code for a different Python version than the default installation, change the
compilation command accordingly (e.g. to python3 setup.py build_ext --inplace).

Run the program first put the file to process in the folder 'application\\inputData'. Then run the following command from the terminal, standing in the 'application' folder:
'python app.py nameOfInput.vtk fibreRadius', where fibreRadius must be a positive integer.


Testing the program
---
There is an option to test the program, using simple input structures. To do this, uncomment the line
'analyze(nzTangents, nzCurvatures, filename, fiber_width, curvature)' in the file
'application\\programWrapper' and run the program using input

In the folder 'application\\data\\testfiles' are several small and simple input structures to
test the program with. Accompanying some of these input files are also a few .txt files. These
contain analytically calculated curvatures to compare the program output with. To run these, move the files to the folder 'application\\inputData' and then run the command
'python app.py nameOfInput.vtk fibreRadius nameOfInput.txt'. The part nameOfInput.txt is optional and only
possible when there is an accompanying .txt file to the input file.


Running without Cython
---
In the folder 'nonCythonAlternatives', are files needed to run the program without the Cython files.
To use these, put the in the folders 'app\\curvature' and 'app\\tangents\\eigenvectors' and switch to
the wrappers in those folders to use these files instead.
