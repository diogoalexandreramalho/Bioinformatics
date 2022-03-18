function [optimal_score, optimal_aligns] = global_align(S1, S2, match, mismatch, gap_penalty)
    
    s_S1 = length(S1);
    s_S2 = length(S2);
    
    % traceability matrix
    H = zeros(s_S1 + 1, s_S2 + 1);
    
    % initialize matrix
    H(:,1) = 0:gap_penalty:(gap_penalty*s_S1);
    H(1,:) = 0:gap_penalty:(gap_penalty*s_S2);
    
    for i = 1:s_S1
        for j = 1:s_S2
            if(S1(i) == S2(j))
                match_value = match;
            else
                match_value = mismatch;
            end
            
            H(i+1,j+1) = max([H(i,j+1)+gap_penalty, H(i+1,j)+gap_penalty, H(i,j)+match_value]);
        end
    end
    
    % get optimal score
    optimal_score = H(s_S1+1, s_S2+1);
    
    % calculate the best alignments
    optimal_aligns = get_best_aligns(S1, S2, H, match, mismatch, gap_penalty, s_S1+1, s_S2+1, {''}, '', '');
end

function best_aligns = get_best_aligns(S1, S2, H, match, mismatch, gap_penalty, curr_i, curr_j, prev_best_substrings, addS1, addS2)
   
    % update with the new characters
    for i = 1:length(prev_best_substrings)
        prev = prev_best_substrings{i};
        sz = length(prev)/2;
        prev_best_substrings{i} = strcat(addS1, prev(1:sz), addS2, prev(sz+1:end));
    end

    % termination condition
    if(curr_j == 1 && curr_i == 1)
        % divide string to distinguish
        for i = 1:length(prev_best_substrings)
            prev = prev_best_substrings{i};
            sz = length(prev)/2;
            prev_best_substrings{i} = strcat(prev(1:sz), '|', prev(sz+1:end));
        end
        
        best_aligns = prev_best_substrings;
        
        return;
    end
    
    % initialize 3 possible paths
    up_best_aligns = [];
    left_best_aligns = [];
    diag_best_aligns = [];
    
    % test 'up'
    if(curr_i > 1)
        if(H(curr_i, curr_j) - gap_penalty == H(curr_i-1, curr_j))
            up_best_aligns = get_best_aligns(S1, S2, H, match, mismatch, gap_penalty, curr_i-1, curr_j, prev_best_substrings, S1(curr_i-1), '-');
        end
    end
    
    % test 'left'
    if(curr_j > 1)
        if(H(curr_i, curr_j) - gap_penalty == H(curr_i, curr_j-1))
            left_best_aligns = get_best_aligns(S1, S2, H, match, mismatch, gap_penalty, curr_i, curr_j-1, prev_best_substrings, '-', S2(curr_j-1));
        end
    end
    
    % test 'diag'
    if(curr_i > 1 && curr_j > 1)
        if(S1(curr_i-1) == S2(curr_j-1))
            match_value = match;
        else
            match_value = mismatch;
        end
        
        if(H(curr_i, curr_j) - match_value == H(curr_i-1, curr_j-1))
            diag_best_aligns = get_best_aligns(S1, S2, H, match, mismatch, gap_penalty, curr_i-1, curr_j-1, prev_best_substrings, S1(curr_i-1), S2(curr_j-1));
        end
    end
    
    best_aligns = [up_best_aligns; diag_best_aligns; left_best_aligns];
end
