%%
clc, clear all, clf
N = 22;
X = zeros(N, N, N);
K = zeros(N, N, N);

R = 8;
rSmall = 2;
r = linspace(0, rSmall);
t = linspace(0, 2 * pi, 1000);
% i = u, j = v
for i = t
    for j = t
        for k = r
            x = R * cos(i) + k .* cos(i) .* cos(j);
            y = R * sin(i) + k .* sin(i) .* cos(j);
            z = k .* sin(j);
            
            if sqrt(x^2 + y^2) < R - rSmall
                disp(x);
            end
            
            x = round(min(max(x + N/2, 1), N));
            y = round(min(max(y + N/2, 1), N));
            z = round(min(max(z + N/2, 1), N));
        
            X(x, y, z) = 1;
            
            K(x, y, z) = 1/( R + k.*cos(j) );
        end
    end
end

ind = find(X);
[i1, i2, i3] = ind2sub(size(X), ind);
plot3(i1, i2, i3, 'o')
axis equal
xlabel('x')
ylabel('y')
zlabel('z')

K = K(find(K));
histogram(K, 40,'Normalization','pdf')
hold on;
meanK = mean(K);
xline(meanK,'LineWidth', 2, 'Color', 'r');
legend('curvatures',['mean: ' num2str(round(meanK,3))])
dlmwrite('torus1Matlab.txt',K)