n=200;
tr_time = zeros(2,n);
calc_time = zeros(2,n);
tt_time = zeros(2,n);
%%
for i = 1:n
    % tic;
    [optimal_score,~,a] = local_align(repmat('ABE',1,i),repmat('DEF',1,i),-4);
    tr_time(:,i) = [i*3; a];
end

%%
close

hold on;
% total time
plot(tt_time(1,:), tt_time(2,:));
x = 3:3:600;
p = polyfit(x, tt_time(2,:), 2);
plot(x, polyval(p, x));
% edit matrix calculation
plot(calc_time(1,:), calc_time(2,:));
% traceback
plot(tr_time(1,:), tr_time(2,:));

legend('Total computational time', 'Quadratic approximation', 'Edit matrix calculation', 'Traceback');
ylabel('Time (s)');
xlabel('Protein length (aa)');
title('Traceback computation time for Smith-Waterman algorithm');