function [V,info] = vtk_read_volume(info)
% Function for reading the volume from a Visualization Toolkit (VTK)
% 
% volume = tk_read_volume(file-header)
%
% examples:
% 1: info = vtk_read_header()
%    V = vtk_read_volume(info);
%    imshow(squeeze(V(:,:,round(end/2))),[]);
%
% 2: V = vtk_read_volume('test.vtk');

if(~isstruct(info)), info=vtk_read_header(info); end

% Open file
fid=fopen(info.Filename,'rb','ieee-be');
% Skip header
fseek(fid,info.HeaderSize,'bof');


if info.NumFields <= 0
    V=cell([1 1]);
    info.NumFields=1;
else
    V=cell([1 info.NumFields]);
end

str=[];

fi=1;
while fi<=info.NumFields

    if isfield(info, 'FieldName') ,
        % read data name, size and type
        while isempty(str), str=fgetl(fid); end;
        if strcmpi(str(1:8),'METADATA')
            str=fgetl(fid);
            s=find(str==' ');
            nrinfo = sscanf(str(s(1)+1:end),'%d');
            for nl = 1:nrinfo
                str=fgetl(fid);
                str=fgetl(fid);
            end
            str=fgetl(fid);
        end
        while isempty(str), str=fgetl(fid); end;
        
        s=find(str==' ');
        info.DataName{fi} = str(1:s(1)-1);
        info.NumberOfComponents{fi} = sscanf(str(s(1)+1:s(2)-1),'%d');
        info.DataType{fi} = strtrim(str(s(3)+1:end));
%         if info.DatasetFormat(1) == 'b'
%             switch info.DataType{fi}
%                 case 'float', datasize = datasize * 4;
%                 case 'double', datasize = datasize * 8;
%                     % NOTE: list is incomplete
%             end
%         end
        
    elseif strcmp(info.DatasetType,'polydata')
        
        if fi > 1
            % first time, read positions, then
            % read data name, size and type
            while ~feof(fid) && (isempty(str) || ~isempty(strfind(lower(str),'point_data'))),
                str=fgetl(fid);
            end;
            
            if ~feof(fid)
                info.NumFields = info.NumFields + 1;
                
                tokens = regexp(str, '\s+', 'split');
                switch lower(tokens{1}),
                    case 'scalars',
                        info.DataName{fi} = tokens{2};
                        info.NumberOfComponents{fi} = sscanf(tokens{4},'%d');
                        info.DataType{fi} = tokens{3};
                        str=fgetl(fid); % read 'LOOKUP_TABLE' line
                    case {'vectors','normals'},
                        info.DataName{fi} = tokens{2};
                        info.NumberOfComponents{fi} = 3;
                        info.DataType{fi} = tokens{3};
                        %case 'tensors',
                end
            else
                break;
            end
        else
            info.NumFields = info.NumFields + 1;
        end
    end
    
    % Read the Data
    sz=prod(info.Dimensions) * info.NumberOfComponents{fi};
    switch(lower(info.DatasetFormat(1)))
        case 'b'
            switch(info.DataType{fi})
                case 'char'
                     V{fi} = int8(fread(fid,sz,'int8')); 
                case 'uchar'
                    V{fi} = uint8(fread(fid,sz,'uint8')); 
                case 'short'
                    V{fi} = int16(fread(fid,sz,'int16')); 
                case 'ushort'
                    V{fi} = uint16(fread(fid,sz,'uint16')); 
                case 'int'
                     V{fi} = int32(fread(fid,sz,'int32')); 
                case 'uint'
                     V{fi} = uint32(fread(fid,sz,'uint32')); 
                case 'float'
                     V{fi} = single(fread(fid,sz,'single'));   
                case 'double'
                    V{fi} = double(fread(fid,sz,'double'));
            end
        case 'a'
            switch(info.DataType{fi})
                case 'char', type='int8';
                case 'uchar', type='uint8';
                case 'short', type='int16';
                case 'ushort', type='uint16';
                case 'int', type='int32';
                case 'uint', type='uint32';
                case 'float', type='single';
                case 'double', type='double';
                otherwise, type='double';
            end
            
            V{fi}=zeros([1 sz],type);
            V{fi} = fscanf(fid,'%f',sz);
            %nr=0;
            %while nr<t, 
            %    vals = str2num(fgetl(fid)); 
            %    V{fi}(nr+1:nr+numel(vals))=vals;
            %    nr = nr + numel(vals);
            %end
    end
    
    if info.NumberOfComponents{fi} > 1,
        dims = [info.NumberOfComponents{fi} info.Dimensions];
    elseif length(info.Dimensions)==1
        dims = [1 info.Dimensions];
    else
        dims = info.Dimensions;
    end
    V{fi} = reshape(V{fi},dims);
    if isscalar(info.Dimensions)
        V{fi} = V{fi}';
    end
    str = fgetl(fid);
    
    fi = fi + 1;
end

fclose(fid);

if info.NumFields == 1
    V = V{1};
end



