function  M = helixWriter(distance, radius, gap)
  d = distance;
  r = radius;

  z=linspace(0,distance,1000);
  t=(2*pi/gap)*z;

  % Each
  z = round(10*z)+1;
  x = round(100*r*cos(t)) + 200+1;
  y = round(100*r*sin(t))+ 200+1;

  plot3(x,y,z)

  % Create empty grid and save the above pixels as 1s
  M = zeros(401,401,401);
  A = [x;y;z];

  for i = 1:1000
      tmp = A(:,i);  % index which should be a 1 in M
      M(tmp(1), tmp(2), tmp(3)) = 1;
  end

end
