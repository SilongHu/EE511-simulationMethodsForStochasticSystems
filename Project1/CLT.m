%Take your Bernoulli success counting routing
%1 represents Success,0 represents Fail
%In this function, the original data has been normalized
function result = CLT(k)
    %result = binornd(k,0.5,1,300);
    Prob = 0.5;
    test = zeros(k,300);
    result = zeros(1,300);
    for n = 1:k
        for i=1:300
            toss = 0;
            for p = 1:5
                toss = 1 - (rand(1)< Prob) + toss ;%if 1 shows less than 50, toss = 0 (fail)
            end
            test(n,i) = toss;
        end
        test(n,:) =  test(n,:) - 2.5; % minus the mean,B(5,0.5) Ex = 2.5, leave the std to bell curve
        result(1,:) = result(1,:) + test(n,:);
    end
    [mu,s] = normfit(result);
    histogram(result,'BinWidth',0.2,'Normalization','probability','DisplayStyle','bar')
    hold on
    x = [-3*s:0.01:3*s];
    norm = normpdf(x,0,sqrt(k*1.25)); % Binomial Distribution, Ex = np, Var = np(1-p)
    plot(x, norm,'linewidth', 2, 'color', 'r')
    str1 = sprintf('Combination of Hist and Plot For 300 Samples Of Sum k = %d  Random Variable',k);
    title(str1);
    str2 = sprintf('The Sum Success Time Of k = %d Trials',k);
    xlabel(str2);
    ylabel({'Probability of Successful Times in 300 Trials','And stardard Bell Curve of PDF'});
 
    