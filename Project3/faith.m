clear,clc;
A = load('Trim_faithful.txt');
A = A(:,2:3);
plot(A(:,1),A(:,2),'.');
title('Scatter 2-D Plot of Eruption and Waiting Time');
xlabel('The Duration of the Old Faithful Geyser Eruption');
ylabel('The Waiting Time Between Eruptions');
idx = kmeans(A,2) ;

figure;
plot(A(idx==1,1),A(idx==1,2),'r.','MarkerSize',12)
hold on
plot(A(idx==2,1),A(idx==2,2),'b.','MarkerSize',12)
title('Two Cluster in Scatter');
xlabel('The Duration of the Old Faithful Geyser Eruption');
ylabel('The Waiting Time Between Eruptions');
legend('Cluster 1','Cluster 2',...
       'Location','NW')