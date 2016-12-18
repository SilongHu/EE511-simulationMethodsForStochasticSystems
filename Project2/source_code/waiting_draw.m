X = -log(rand(3000,1))/5;
H1 = histogram(X,'Normalization','probability');

R = exprnd(0.2,[3000,1]);
hold on;
H2 = histogram(R,'Normalization','probability');
legend({'Simulation','Exponential Distribution'});
xlabel('Exponential Random Variable');
ylabel('Probability of Show Time');
title('Simulation Distribution Comparing to Exponential Distribution');