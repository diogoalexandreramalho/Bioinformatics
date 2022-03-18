function [optimal_score, optimal_aligns] = local_align(S1, S2, gap_penalty)
    
    % definition of Blosum50 matrix
    B50 = [
        5,-2,-1,-2,-1,-1,-1, 0,-2,-1,-2,-1,-1,-3,-1, 1, 0,-3,-2, 0;
        -2, 7,-1,-2,-4, 1, 0,-3, 0,-4,-3, 3,-2,-3,-3,-1,-1,-3,-1,-3;
        -1,-1, 7, 2,-2, 0, 0, 0, 1,-3,-4, 0,-2,-4,-2, 1, 0,-4,-2,-3;
        -2,-2, 2, 8,-4, 0, 2,-1,-1,-4,-4,-1,-4,-5,-1, 0,-1,-5,-3,-4;
        -1,-4,-2,-4, 13,-3,-3,-3,-3,-2,-2,-3,-2,-2,-4,-1,-1,-5,-3,-1;
        -1, 1, 0, 0,-3, 7, 2,-2, 1,-3,-2, 2, 0,-4,-1, 0,-1,-1,-1,-3;
        -1, 0, 0, 2,-3, 2, 6,-3, 0,-4,-3, 1,-2,-3,-1,-1,-1,-3,-2,-3;
        0,-3, 0,-1,-3,-2,-3, 8,-2,-4,-4,-2,-3,-4,-2, 0,-2,-3,-3,-4;
        -2, 0, 1,-1,-3, 1, 0,-2, 10,-4,-3, 0,-1,-1,-2,-1,-2,-3, 2,-4;
        -1,-4,-3,-4,-2,-3,-4,-4,-4, 5, 2,-3, 2, 0,-3,-3,-1,-3,-1, 4;
        -2,-3,-4,-4,-2,-2,-3,-4,-3, 2, 5,-3, 3, 1,-4,-3,-1,-2,-1, 1;
        -1, 3, 0,-1,-3, 2, 1,-2, 0,-3,-3, 6,-2,-4,-1, 0,-1,-3,-2,-3;
        -1,-2,-2,-4,-2, 0,-2,-3,-1, 2, 3,-2, 7, 0,-3,-2,-1,-1, 0, 1;
        -3,-3,-4,-5,-2,-4,-3,-4,-1, 0, 1,-4, 0, 8,-4,-3,-2, 1, 4,-1;
        -1,-3,-2,-1,-4,-1,-1,-2,-2,-3,-4,-1,-3,-4, 10,-1,-1,-4,-3,-3;
        1,-1, 1, 0,-1, 0,-1, 0,-1,-3,-3, 0,-2,-3,-1, 5, 2,-4,-2,-2;
        0,-1, 0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1, 2, 5,-3,-2, 0;
        -3,-3,-4,-5,-5,-1,-3,-3,-3,-3,-2,-3,-1, 1,-4,-4,-3, 15, 2,-3;
        -2,-1,-2,-3,-3,-1,-2,-3, 2,-1,-1,-2, 0, 4,-3,-2,-2, 2, 8,-1;
        0,-3,-3,-4,-1,-3,-3,-4,-4, 4, 1,-3, 1,-1,-3,-2, 0,-3,-1, 5
    ];
    % contruct a map for refering to in the B50 matrix
    aminos = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'];
    B50_map = cell(1, length(aminos));
    for i = 1:length(aminos)
        B50_map{aminos(i)} = i;
    end

    s_S1 = length(S1);
    s_S2 = length(S2);
    
    % - Traceability matrix
    % - Initialization of 1st column and row not recquired in Local Alignment
    % since these are all zero at the beginning
    H = zeros(s_S1 + 1, s_S2 + 1);
    
    for i = 1:s_S1
        for j = 1:s_S2
            % get match value from B50
            match_value = B50(B50_map{S1(i)}, B50_map{S2(j)});
            
            H(i+1,j+1) = max([0, H(i,j+1)+gap_penalty, H(i+1,j)+gap_penalty, H(i,j)+match_value]);
        end
    end
    
    optimal_score = max(max(H));
    
    % Initialize optimal alignments
    optimal_aligns = cell(1, sum(H(:)==optimal_score));
    
    % Look for every optimal possible alignments
    cnt = 1;
    for i = 2:s_S1+1
        for j = 2:s_S2+1
            % check for all indices that have the maximum score
            if(H(i,j) == optimal_score)
                k = 0;
                while(H(i-k, j-k) > 0)
                    k = k + 1;
                end
                
                % indices where alignment begins for each string
                k1 = i - k;
                k2 = j - k;
                
                % length of alignment answer
                slack1_beg = i - k - 1;
                slack2_beg = j - k - 1;
                slack1_end = s_S1 - i + 1;
                slack2_end = s_S2 - j + 1;
                len = min([slack1_beg, slack2_beg]) + abs(slack1_beg - slack2_beg) + k + min([slack1_end, slack2_end]) + abs(slack1_end - slack2_end);
                
                % necessary blank spaces
                n_blanks1 = max([0,k2-k1]);
                n_blanks2 = max([0,k1-k2]);
                n_blanks0 = max([k1, k2])-1;
                
                % generate the current optimal alignment
                optimal_aligns{cnt} =   [   [blanks(n_blanks1), S1, blanks(len - n_blanks1 - s_S1)]; 
                                            [blanks(n_blanks0), repmat('|',1,k), blanks(len - n_blanks0 - k)];
                                            [blanks(n_blanks2), S2, blanks(len - n_blanks2 - s_S2)]
                                        ];
                
                cnt = cnt + 1;
            end
        end
    end
end

