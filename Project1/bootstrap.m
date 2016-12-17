A = importdata('NJGAS.dat'); %import the data and store it as a vector
sum = 0;
for i = 1:length(A)
    sum = sum+A(i);
end
avg = sum/length(A);

gather_mean = zeros(1,1000);%store 1000 times sampling mean
for i = 1:1000
    choose = randsample(A,length(A),true);
    %each time pick length(A) samples and count their mean
    sum_sample = 0;
    for j = 1:length(A)
        sum_sample = choose(j) + sum_sample;
    end
    gather_mean(i) = sum_sample/length(A);
end
gather_mean = sort(gather_mean);
CI = gather_mean(25:974);
interval1 = [CI(1),CI(950)];
ci = bootci(1000*length(A),@mean, A);%take the same amount of gether_mean taken
interval2 = ci;
disp(interval1)
disp(interval2)


