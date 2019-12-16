function writeVTK(M,filename,fmtstring)

%WRITEVTK Write data to VTK file
%   WRITEVTK(A,FILENAME) writes the elements of the matrix A to a 
%   file with the specified FILENAME in the legacy VTK format.
%
%   If A is a 3D matrix, the data is written as single precision scalars    
%   on a uniform grid.
%   A may also be a 4D matrix with vector/tensor values along the first 
%   dimension. If size(A,1)==3, the data is written as vectors with the 
%   different vector components along the first matrix dimension.
%   Otherwise, data is written as scalars with size(A,1) components. To
%   avoid confusion, a limit of 9 on the number of components is imposed.
%
%   2D data or multiple arrays in one file is currently not supported.
%
%   WRITEVTK(A,FILENAME,FMT) writes data in the specified format, where FMT
%   may be 'binary' (default) or 'ascii'.
%
%   For example,
%
%      A = randn([3 10 10 10]);
%      writeVTK(A,'randvectors.vtk');
%
%   creates a VTK file with random vectors on a 10x10x10 grid.
%
%   Copyright 2016 Tobias Gebäck


if nargin<3
    fmtstring='binary';
end

% write the matrix M as VTK file
switch fmtstring
    case 'ascii', write_ascii=1;
    case 'binary', write_ascii=0;
    otherwise
        error('Bad value for fmtstring. Must be ''ascii'' or ''binary''.');
end

n=size(M);
ncmp = 1;  % number of components
if length(n) ~= 3 && ~(length(n) == 4 && n(1) <= 9)
    error('M must be a 3-dimensional matrix or a 4-D matrix with size(M,1)<=9!');
end
if length(n)==4
    dims=n(2:4);
    ncmp = n(1);
else
    dims=n;
end

f=fopen(filename,'w');

fprintf(f,'# vtk DataFile Version 3.0\n');
fprintf(f,'Genereated by Matlab writeVTK()\n');
if write_ascii
    fprintf(f,'ASCII\n');
else
    fprintf(f,'BINARY\n');
end
fprintf(f,'DATASET STRUCTURED_POINTS\n');
fprintf(f,'DIMENSIONS %d %d %d\n', dims(1), dims(2), dims(3));
fprintf(f,'ORIGIN 0 0 0\n');
fprintf(f,'SPACING 1 1 1\n');

fprintf(f,'POINT_DATA %d\n', prod(dims));
if ncmp ~= 3
    fprintf(f,'SCALARS value float %d\n',ncmp);
    fprintf(f,'LOOKUP_TABLE default\n');
    if write_ascii
        fprintf(f,'%g\n',M(:));
    else
        fwrite(f,single(M(:)),'single','ieee-be');
    end
else
    fprintf(f,'VECTORS vector float\n');
    if write_ascii
        fprintf(f,'%g %g %g\n', M(:)');
    else
        fwrite(f,single(M(:)),'single','ieee-be');
    end
end

fclose(f);
