%Count the number of successes in 5 fair Bernoulli trials
%1 represents Success,0 represents Fail
result = zeros(1,100);
prob = 0.5;
% 100 trials
for i=1:100
    toss = 0;
    for j = 1:5 % Count to 5
        toss = 1 - (rand(1) < prob) + toss; % record the success time
    end
    result(i) = toss;
end

histogram(result,'Normalization','count','DisplayStyle','bar')
title('A Histogram For 100 Samples Of Counting Random Variable')
xlabel('Success Times in 5 fair Bernuolli Trials ')
ylabel('Numbers in 100 trials of Each Successful Show Times')