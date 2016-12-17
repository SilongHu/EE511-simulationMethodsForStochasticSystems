%Toss a coin 100 times
%1 represents HEAD,0 represents TAIL
a = zeros(1,100); %Store 100 trials' result
prob = 0.5;% the probability to get HEAD
for i=1:100
    a(i) = rand(1) < prob;%randomly generate a number from 0-1;
end
axis([0:1 0 100]);
histogram(a,'BinWidth',0.2,'Normalization','count','DisplayStyle','bar')
title('A Histogram For 100 Simulated Bernoulli Trial');
xlabel('0(Tail) And 1(Head)');
ylabel('Show Time');