function X = newhelixWriter(inner_radius, outer_radius, height_per_revolution, revolutions)

    h = height_per_revolution;
    r = inner_radius;
    R = outer_radius;
    n = revolutions;
    
    X = zeros(2*R*r + 1, 2*R*r + 1, h*n + 2*r);
    
    tr = linspace(0, 2*pi, 100*r);
    tR = linspace(0, 2*pi*r, 100*r);
    
    for i = tR
        for j = tr
            for k = linspace(0, r, 10*r)
                
                x = R * cos(i) + k .* cos(i) .* cos(j);
                y = R * sin(i) + k .* sin(i) .* cos(j);
                z = k .* sin(j) + i .* h;
                
                x = x + R + r + 1;
                y = y + R + r + 1;
                z = z + r + 1;
                
                x = round(x);
                y = round(y);
                z = round(z);
                
                X(x, y, z) = 1;
                
            end
        end
    end
    
    ind = find(X);
    [i1, i2, i3] = ind2sub(size(X), ind);
    plot3(i1, i2, i3, 'o')
    xlabel('x')
    ylabel('y')
    axis equal
end


