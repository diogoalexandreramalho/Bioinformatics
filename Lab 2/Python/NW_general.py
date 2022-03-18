import numpy as np

def NW_general(initial_s1,initial_s2,match,mismatch,gap):


    ##########################
    #	  Initialization     #
    ##########################

    # Dict with paths in the shape {path_number: [[i_pos,j_pos],"seq_1","seq_2"]}
    paths = {}

    # has all the paths that are not yet finished
    unfinished_paths = []

    path_index = 0
    next_i = 0
    next_j = 0

    s1_list = initial_s1.split(",")
    s2_list = initial_s2.split(",")
    no_seq1 = len(s1_list)
    no_seq2 = len(s2_list)
    initial_s1_len = len(s1_list[0])
    initial_s2_len = len(s2_list[0])


    ##########################
    #		Functions        #
    ##########################

    def w(x, y):
        if (x == '-' and y == '-'):
            return 0
        elif (x == y):
            return match
        elif (x == '-' or y == '-'):
            return gap
        else:
            return mismatch


    def score(index_seq1, index_seq2, score_type):
        seq1_elements = []
        seq2_elements = []

        sum = 0

        if score_type == 0:
            for i in range(no_seq1):
                seq1_elements = np.append(seq1_elements, s1_list[i][index_seq1])
            for j in range(no_seq2):
                seq2_elements = np.append(seq2_elements, s2_list[j][index_seq2])
            for k in range(no_seq1):
                for l in range(no_seq2):
                    sum += w(seq1_elements[k], seq2_elements[l])

        elif score_type == 1:
            for i in range(no_seq1):
                seq1_elements = np.append(seq1_elements, s1_list[i][index_seq1-1])
            for k in range(no_seq1):
                sum = sum + w(seq1_elements[k], '-')
            sum *= no_seq2

        else:
            for j in range(no_seq2):
                seq2_elements = np.append(seq2_elements, s2_list[j][index_seq2-1])
            for l in range(no_seq2):
                sum += w('-', seq2_elements[l])
            sum *= no_seq1

        return sum


    # creates a new path with a position and sequences
    def create_new_path(i, j, seq_1, seq_2, path_index):
        paths[path_index] = [[i, j], seq_1, seq_2]
        flag_more_paths = 1
        unfinished_paths.append(path_index)
        path_index += 1
        return path_index


    # updates the position and sequences of a certain path
    def update_path(i, j, seq_1, seq_2):
        paths[current_index] = [[i, j], seq_1, seq_2]
        next_i = i
        next_j = j
        flag_more_paths = 1
        return [next_i, next_j], flag_more_paths


    def add_seq(new, seq):
        new_seq = []
        for i in range(len(seq)):
            new_seq.append(new[i] + seq[i])
        return new_seq


    def find_in_seq1(index):
        found_list = []
        for i in range(no_seq1):
            found_list.append(s1_list[i][index])
        return found_list


    def find_in_seq2(index):
        found_list = []
        for i in range(no_seq2):
            found_list.append(s2_list[i][index])
        return found_list


    ##########################
    #		   Code          #
    ##########################

    # Create matrix
    F = np.zeros((initial_s1_len + 1, initial_s2_len + 1), dtype=int)

    F[0, 0] = 0
    # Initialize matrix with F(i,0) = -id and F(0,j)=-jd
    for i in range(initial_s1_len):
        F[i + 1, 0] = F[i, 0] + score(i + 1, 0, 1)

    for j in range(initial_s2_len):
        F[0][j + 1] = F[0, j] + score(0, j + 1, 2)

    # Calculate matrix values
    for i in range(1, initial_s1_len + 1):
        for j in range(1, initial_s2_len + 1):
            F[i, j] = max(F[i - 1, j - 1] + score(i - 1, j - 1, 0), F[i - 1, j] + no_seq1 * no_seq2 * gap,
                          F[i, j - 1] + no_seq2 * no_seq1 * gap)

    # Define the value in last column and last row as the start of traceback
    paths[path_index] = [[initial_s1_len, initial_s2_len], [''] * no_seq1, [''] * no_seq2]
    unfinished_paths.append(path_index)
    path_index += 1

    # Do the traceback for all the paths
    while len(unfinished_paths) != 0:

        # Choose next path to trace
        current_index = unfinished_paths[0]
        i = paths[current_index][0][0]
        j = paths[current_index][0][1]

        while (i, j) != (0, 0):

            flag_more_paths = 0

            s1 = paths[current_index][1]
            s2 = paths[current_index][2]

            if F[i - 1, j - 1] + score(i - 1, j - 1, 0) == F[i, j]:
                new_elements_1 = find_in_seq1(i - 1)
                new_elements_2 = find_in_seq2(j - 1)
                next_pos, flag_more_paths = update_path(i - 1, j - 1, add_seq(new_elements_1, s1), add_seq(new_elements_2, s2))

            if F[i - 1, j] + no_seq1 * no_seq2 * gap == F[i, j]:
                new_elements_1 = find_in_seq1(i - 1)
                if flag_more_paths:
                    path_index = create_new_path(i - 1, j, add_seq(new_elements_1, s1), add_seq(['-'] * no_seq2, s2),
                                                 path_index)
                else:
                    next_pos, flag_more_paths = update_path(i - 1, j, add_seq(new_elements_1, s1),
                                                            add_seq(['-'] * no_seq2, s2))

            if F[i, j - 1] + no_seq2 * no_seq1 * gap == F[i, j]:
                new_elements_2 = find_in_seq2(j - 1)
                if flag_more_paths:
                    path_index = create_new_path(i, j - 1, add_seq(['-'] * no_seq1, s1), add_seq(new_elements_2, s2),
                                                 path_index)
                else:
                    next_pos, flag_more_paths = update_path(i, j - 1, add_seq(['-'] * no_seq1, s1),
                                                            add_seq(new_elements_2, s2))

            i = next_pos[0]
            j = next_pos[1]

        del unfinished_paths[0]

    # Print optimal alignments and scores
    alignments = []
    final_score = F[initial_s1_len, initial_s2_len]

    for path in paths:
        #print("\n{:d}.\t{}\n  \t{}\n  Score: {:d}".format(path + 1, paths[path][1], paths[path][2], F[initial_s1_len, initial_s2_len]))
        alignments.append(paths[path][1] + paths[path][2])

    print(F)

    return alignments, final_score

