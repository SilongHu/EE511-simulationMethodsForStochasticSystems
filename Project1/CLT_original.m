%Take your Bernoulli success counting routing
%1 represents Success,0 represents Fail
%In this function, the original data has been normalized
function result = CLT_original(k)
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
        result(1,:) = result(1,:) + test(n,:);
    end
    histogram(result,'BinWidth',0.2,'Normalization','probability','DisplayStyle','bar')
    hold on
    x = [min(result):0.01:max(result)];
    norm = normpdf(x,2.5*k,sqrt(1.25*k)); % Binomial Distribution, Ex = np, Var = np(1-p)
    plot(x, norm,'linewidth', 2, 'color', 'r')
    str1 = sprintf('Combination of Hist and Plot For 300 Samples Of Sum k = %d  Random Variable',k);
    title(str1);
    str2 = sprintf('The Sum Success Time Of k = %d Trials',k);
    xlabel(str2);
    ylabel({'Probability of Successful Times in 300 Trials','And stardard Bell Curve of PDF'});
 
    