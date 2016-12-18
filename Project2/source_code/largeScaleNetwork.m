clear,clc;

p = 0.08;% Change the P value
n = 250; % Change the Node number
A = VD(p,n);
H1 = histogram(A,'Normalization','probability');
 
%Compare to poisson distribution
hold on;
pd = fitdist(A','poisson');
R = poissrnd(pd.lambda,[1,length(A)]);
H2 = histogram(R,'Normalization','probability');
legend({'Simulation','Poisson Distribution'});

xlabel('The Number of Vertex Degree');
ylabel('Probability of Corresponding Degree');
str = sprintf('Histogram of Vertex Degrees for Networks of p=%.2f With %d Nodes',p,n);
title(str);


[N] = histcounts(A);
bins = min(A):max(A);
n = sum(N);
pd = fitdist(bins','Poisson','Frequency',N');
expCounts = n * pdf(pd,bins); 
[H P STAT] = chi2gof(bins,'Ctrs',bins,...
        'Frequency',N,'Expected',expCounts,'nparam',0,'Alpha',0.05);

function VertexDegree = VD(p,n)
    edge=random('Binomial',1,p,n,n);
    edge(edge==0)=-1;
    edge=abs(edge'+edge);
    edge(edge==0)=1;
    edge(edge~=1)=0;
    VertexDegree = zeros(1,n);
    for i = 1:n
        VertexDegree(i)=nnz(edge(i,:));
    end
end
