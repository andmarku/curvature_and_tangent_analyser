%%

N = 200;
X = zeros(N, N, N);

R = 50;

r = linspace(0, 3);
t = linspace(0, 2 * pi, 1000);

for i = t
    for j = t
        for k = r
            x = R * cos(i) + k .* cos(i) .* cos(j);
            y = R * sin(i) + k .* sin(i) .* cos(j);
            z = k .* sin(j);
            
            if sqrt(x^2 + y^2) < R - 3
                disp(x);
            end
            
            x = round(min(max(x + N/2, 1), N));
            y = round(min(max(y + N/2, 1), N));
            z = round(min(max(z + N/2, 1), N));
        
            X(x, y, z) = 1;
        end
    end
end

ind = find(X);
[i1, i2, i3] = ind2sub(size(X), ind);
plot3(i1, i2, i3, 'o')
axis equal