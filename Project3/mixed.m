clear,clc;
R1 = normrnd(-1,1,[1,1000]);
R2 = normrnd(1,1,[1,1000]);
mu  = [-1 1];
std = [1 1];
N = 1000;
r = rand(1,N);
x1 = (r > 0.6).*R1;
x2 = (r <= 0.6).*R2;
%x1 = (r >0.6).*(mu(1) + std(1)*randn(1,N));
%x2 = (r<=0.6).*(mu(2) + std(2)*randn(1,N));
x = x1+x2;
%figure;
%hold on
histogram(x,30,'Normalization','probability');
title('Histogram of Mixture Distribution');
xlabel('f(x) Value');
ylabel('Probability');


A = x';
%A = [x1;x2]';
idx = kmeans(A,2) ;
A1 = A(idx==1);
A2 = A(idx==2);
figure;
histogram(A1,'Normalization','probability');
hold on
histogram(A2,'Normalization','probability');

title('Two Cluster in Histogram of Mixture Distribution');
xlabel('Two Cluster Value');
ylabel('Probability');
legend('Cluster 1','Cluster 2',...
       'Location','NW')
%{
figure;
plot(A(idx==1,1),A(idx==1,2),'r.','MarkerSize',12)
hold on
plot(A(idx==2,1),A(idx==2,2),'b.','MarkerSize',12)
%}