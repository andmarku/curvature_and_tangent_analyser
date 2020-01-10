%%
clc, clear all
N = 50;
X = zeros(N, N, N);
K1 = zeros(N, N, N);
K2 = zeros(N, N, N);

R = 15;

r = linspace(0, 3);
t = linspace(0, 2 * pi, 1000);
% i = u, j = v
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
            
            K1(x, y, z) = -cos(j)/( R + k*cos(j) );
            K2(x, y, z) = -1/k;
        end
    end
end

ind = find(X);
[i1, i2, i3] = ind2sub(size(X), ind);
plot3(i1, i2, i3, 'o')
xlabel('x')
ylabel('y')
zlabel('z')
axis equal
Test = K1.*K2
histogram(K1(find(K1)), 35)
% Ktest = round(K1, 2)
