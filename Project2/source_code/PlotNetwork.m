clear,clc;
%function edge = PlotNetwork(p,n)
p = 0.09;
n = 50;
matrix = Plot(p,n);

function edge = Plot(p,n)
    %Create a random edge matrix with n nodes
    %simulate bernoulli trail
    edge=random('Binomial',1,p,n,n);
    edge(edge==0)=-1;
    edge=abs(edge'+edge);
    edge(edge==0)=1;
    figure;
    G=graph(edge==1);
    plot(G);
    axis off;
    str = sprintf('Plot Networks of p=%.2f With %d Nodes',p,n);
    title(str);
end
   