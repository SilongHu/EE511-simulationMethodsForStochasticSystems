%Each exponential random sample represents the waiting time until an event occurs. 
%Implement a routine to count the number of events that occur in 1 unit of time. 
%Generate such counts for 1000 separate unit time intervals. 
%How are these counts distributed? Justify your answer 
clear; clc;

res = -log(rand(1,5000))/5; %The CDF inverse exp distribution
count = zeros(1,1000); %Record the number of events 
% that occur in 1 unit of time for 1000 separate intervals.
k = 1;
for i = 1:1000
summ = 0; %The unit interval
time = 0; % The counter
    while summ < 1
        summ = summ + res(k);
        k = k + 1;
        if (k > 5000) %if exceed the boundary, start again.
            k = 1;
        end
        time = time + 1;
    end
    count(i) = time - 1; %Minus 1 because adding last one is larger than 1
end

%Hist the counting distribution
H1 = histogram(count,'Normalization','probability','BinMethod','auto');
%{
xlabel('The Number of Events That Occur in 1 Unit of Time');
ylabel('Probability of Corresponding Time');
title('Counting Distribution');
%}
hold on;
%Compare it to the Poisson Distribution
R = poissrnd(5,[1,1000]);
H2 = histogram(R,'Normalization','probability','BinMethod','auto');

legend({'Simulation','Poisson Distribution'});
xlabel('The Number of Events That Occur in 1 Unit of Time');
ylabel('Probability of Corresponding Time');
title('Counting Distribution Comparing to Poisson Distribution');

%Test for a Possion Distribution using chi2gof
%Method 1:
[N] = histcounts(count);
bins = min(count):max(count);
n = sum(N);
pd = fitdist(bins','Poisson','Frequency',N');
%lambdaHat = sum(bins.*N)/n;
%expCounts = n * poisspdf(bins,lambdaHat);
expCounts = n * pdf(pd,bins); 
[H P STAT] = chi2gof(bins,'Ctrs',bins,...
        'Frequency',N,'Expected',expCounts,'nparam',0,'Alpha',0.05);
%Method 2
%X = count';
%[H P STATS] = chi2gof(X,'cdf',@(z)poisscdf(z,mean(X)),'Alpha',0.05,'nparam',1);
