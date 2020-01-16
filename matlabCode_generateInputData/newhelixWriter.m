function X = newhelixWriter(inner_radius, outer_radius, height_per_revolution, revolutions, filename)

    h = height_per_revolution;
    r = inner_radius;
    R = outer_radius;
    n = revolutions;
    
    % Matrix limits
    xLimit = ceil(2*R + 2*r);
    yLimit = ceil(2*R + 2*r);
    zLimit = ceil(2*h*n*pi + 2*r);
    
    % Give extra space to limits
    xLimit = xLimit + ceil(2*r);
    yLimit = yLimit + ceil(2*r);
    zLimit = zLimit + ceil(2*r);
    
    X = zeros(xLimit, yLimit, zLimit);
    K = zeros(xLimit, yLimit, zLimit);
    
    tr = linspace(0, 2*pi, ceil(100*r));
    tR = linspace(0, 2*pi*n, ceil(100*r));
    
    for i = tR
        for j = tr
            for k = linspace(0, r, ceil(10*r))
                
                x = R * cos(i) + k .* cos(i) .* cos(j);
                y = R * sin(i) + k .* sin(i) .* cos(j);
                z = k .* sin(j) + i .* h;
                
                % Offset to origin
                x = x + xLimit/2;
                y = y + yLimit/2;
                z = z + zLimit/2;
                
                x = round(x);
                y = round(y);
                z = round(z);
                
                X(x, y, z) = 1;
                % Torus curvature
                %K(x, y, z) = 1/(R + k.*cos(j));
                % Helix curvature
                K(x, y, z) = (R + k.*cos(j))/((R + k.*cos(j))^2 + h^2);
            end
        end
    end
    
    figure(1)
    ind = find(X);
    [i1, i2, i3] = ind2sub(size(X), ind);
    plot3(i1, i2, i3, 'o')
    xlabel('x')
    ylabel('y')
    axis equal

    figure(2)
    K = K(K ~= 0);
    histogram(K, 40, 'Normalization', 'pdf')
    hold on;
    meanK = mean(K);
    xline(meanK, 'LineWidth', 2, 'Color', 'r');
    legend('curvatures', ['mean: ' num2str(round(meanK, 3))])
    dlmwrite(filename+".txt", K)
    
    writeVTK(X, filename+".vtk")
end


