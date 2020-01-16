%%

N = 20;

X = zeros(N, N, N);

X(4, 10, 10) = 1;
X(4, 10, 11) = 1;
X(4, 11, 10) = 1;
X(4, 11, 11) = 1;

for i = 5:15
	X(i, 10, 10) = 1;
	X(i, 10, 11) = 1;
	X(i, 11, 10) = 1;
	X(i, 11, 11) = 1;
	
	X(i, 9, 10) = 1;
	X(i, 9, 11) = 1;

	X(i, 12, 10) = 1;
	X(i, 12, 11) = 1;

	X(i, 10, 9) = 1;
	X(i, 11, 9) = 1;

	X(i, 10, 12) = 1;
	X(i, 11, 12) = 1;
end

X(16, 10, 10) = 1;
X(16, 10, 11) = 1;
X(16, 11, 10) = 1;
X(16, 11, 11) = 1;

writeVTK(X, 'file.vtk')