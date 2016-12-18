clear; clc;
for sim =1:1000
    X = -log(rand(100,1))/5;%The CDF inverse exp distribution
    test_cdf = makedist('exp', 'mu', 0.2);
    [h(sim), p(sim)] = kstest(X, 'CDF', test_cdf,'Alpha',0.05);
end
str = sprintf('The number of rejection cases is %d',nnz(h));
disp(str)