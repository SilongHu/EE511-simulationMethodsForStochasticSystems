%Count the number of trials before the first successful Bernoulli trial
result = zeros(1,100);%store the counting ramdon variable.
% 100 trials
for i=1:100
    toss = 0;
    count = 0;
    while(toss == 0) 
        % if the trial is still fail, go ahead,count the number until success
        toss = 1 - (rand(1)<0.5);
        count = count + 1;
    end
    result(i) = count;
end

histogram(result,'Normalization','count','DisplayStyle','bar')
title('A Histogram For 100 Samples Of Counting Random Variable')
xlabel('The Number Of Trials Before The First Successful Bernoulli Trial')
ylabel('Numbers in 100 trials of Each Successful Times')