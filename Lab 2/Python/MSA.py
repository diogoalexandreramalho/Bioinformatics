import numpy as np
from NW_general import NW_general
import math
import copy


def MSA(seq_list, match, mismatch, gap):
    ##########################
    #		Functions        #
    ##########################

    def conversionToMatrixCoord(int, no_sequence):
        j = int % no_sequence
        i = int // no_sequence
        return i, j

    def build_distanceMatrix(seq_list):
        no_sequences = len(seq_list)
        distance_matrix = np.ones((no_sequences, no_sequences))
        distance_matrix.fill(-math.inf)
        for i in range(no_sequences):
            for j in range(i + 1, no_sequences):
                alignments, final_score = NW_general(seq_list[i], seq_list[j], match, mismatch, gap)
                distance_matrix[i, j] = final_score
        return distance_matrix

    def distanceMatrix_metric(DM):
        sum = 0
        no_sequences = len(DM)
        if no_sequences>1:
            no_combinations = math.factorial(no_sequences)/(math.factorial(no_sequences-2)*2)
            for i in range(no_sequences):
                for j in range(no_sequences):
                    if DM[i,j] != -math.inf:
                        sum += DM[i,j]
            mean = sum/no_combinations
            return mean
        else:
            return 0

    def find_in_seq(index):
        found_list = []
        for i in range(no_seq):
            found_list.append(sequences_aligned[i][index])
        return found_list

    def w(x, y):
        if (x == '-' and y == '-'):
            return 0
        elif (x == y):
            return match
        elif (x == '-' or y == '-'):
            return gap
        else:
            return mismatch

    ##########################
    #	  Initialization     #
    ##########################

    no_seq = len(seq_list)

    ##########################
    #		Code             #
    ##########################
    while len(seq_list) != 1:

        # Distance-matrix
        DM = build_distanceMatrix(seq_list)
        no_sequence = len(DM)
        max_integer_coordinate = DM.argmax()
        max_matrix_coordinate = conversionToMatrixCoord(max_integer_coordinate, no_sequence)
        s1_index = max_matrix_coordinate[0]
        s2_index = max_matrix_coordinate[1]


        alignments, final_score = NW_general(seq_list[s1_index], seq_list[s2_index], match, mismatch, gap)
        del (seq_list[s1_index])
        del (seq_list[s2_index-1])
        
        # Choose best alignment
        best_alignment_score = -math.inf
        for i in range(len(alignments)):
            alignments[i] = ','.join(alignments[i])
            new_seq_list = copy.copy(seq_list)
            new_seq_list.append(alignments[i])
            DM = build_distanceMatrix(new_seq_list)
            alignment_score = distanceMatrix_metric(DM)
            if alignment_score > best_alignment_score:
                best_alignment_score = alignment_score
                best_alignment = alignments[i]

        seq_list.append(best_alignment)

    #Sum of pairs

    sequences_aligned = seq_list[0].split(',')
    sequence_size = len(sequences_aligned[0])
    sum_of_pairs = 0
    for i in range(sequence_size):
        ith_elements = find_in_seq(i)
        for j in range(no_seq):
            for k in range (j+1,no_seq):
                sum_of_pairs += w(ith_elements[j],ith_elements[k])

    return sequences_aligned, sum_of_pairs

