function result = fatherFun(input)
    % This is the main function that depends on b.m
    % Perform some computations using functions from both a.m and b.m
    result = sonFun(input) * 2;
end
