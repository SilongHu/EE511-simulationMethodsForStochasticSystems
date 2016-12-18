%Use the inverse CDF method to generate independent samples,
%Xi, of the exponential random variable with average waiting time of 0.2 time units. 
%Evaluate the quality of your generator with goodness of fit tests. 
clear; clc;
for sim = 1:1000
    X = -log(rand(3000,1))/5;%The CDF inverse exp distribution
    [H(sim) P(sim) STATS] = chi2gof(X,'cdf',@(z)expcdf(z,mean(X)),'Alpha',0.05,'nparam',1);
end
str = sprintf('The number of rejection cases is %d',nnz(H));
disp(str)