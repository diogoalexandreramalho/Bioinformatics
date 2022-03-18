import numpy as np

blosum50 = {"A": {"A":  5, "R": -2, "N": -1, "D": -2, "C": -1, "Q": -1, "E": -1, "G":  0, "H": -2, "I": -1, "L": -2, "K": -1, "M": -1, "F": -3, "P": -1, "S":  1, "T":  0, "W": -3, "Y": -2, "V":  0},
			"R": {"A": -2, "R":  7, "N": -1, "D": -2, "C": -4, "Q":  1, "E":  0, "G": -3, "H": 0 , "I": -4, "L": -3, "K":  3, "M": -2, "F": -3, "P": -3, "S": -1, "T": -1, "W": -3, "Y": -1, "V": -3},
			"N": {"A": -1, "R": -1, "N":  7, "D":  2, "C": -2, "Q":  0, "E":  0, "G":  0, "H": 1 , "I": -3, "L": -4, "K":  0, "M": -2, "F": -4, "P": -2, "S":  1, "T":  0, "W": -4, "Y": -2, "V": -3},
			"D": {"A": -2, "R": -2, "N":  2, "D":  8, "C": -4, "Q":  0, "E":  2, "G": -1, "H": -1, "I": -4, "L": -4, "K": -1, "M": -4, "F": -5, "P": -1, "S":  0, "T": -1, "W": -5, "Y": -3, "V": -4}, 
			"C": {"A": -1, "R": -4, "N": -2, "D": -4, "C": 13, "Q": -3, "E": -3, "G": -3, "H": -3, "I": -2, "L": -2, "K": -3, "M": -2, "F": -2, "P": -4, "S": -1, "T": -1, "W": -5, "Y": -3, "V": -1}, 
			"Q": {"A": -1, "R":  1, "N":  0, "D":  0, "C": -3, "Q":  7, "E":  2, "G": -2, "H":  1, "I": -3, "L": -2, "K":  2, "M":  0, "F": -4, "P": -1, "S":  0, "T": -1, "W": -1, "Y": -1, "V": -3}, 
			"E": {"A": -1, "R":  0, "N":  0, "D":  2, "C": -3, "Q":  2, "E":  6, "G": -3, "H":  0, "I": -4, "L": -3, "K":  1, "M": -2, "F": -3, "P": -1, "S": -1, "T": -1, "W": -3, "Y": -2, "V": -3}, 
			"G": {"A":  0, "R": -3, "N":  0, "D": -1, "C": -3, "Q": -2, "E": -3, "G":  8, "H": -2, "I": -4, "L": -4, "K": -2, "M": -3, "F": -4, "P": -2, "S":  0, "T": -2, "W": -3, "Y": -3, "V": -4}, 
			"H": {"A": -2, "R":  0, "N":  1, "D": -1, "C": -3, "Q":  1, "E":  0, "G": -2, "H": 10, "I": -4, "L": -3, "K":  0, "M": -1, "F": -1, "P": -2, "S": -1, "T": -2, "W": -3, "Y":  2, "V": -4}, 
			"I": {"A": -1, "R": -4, "N": -3, "D": -4, "C": -2, "Q": -3, "E": -4, "G": -4, "H": -4, "I":  5, "L":  2, "K": -3, "M":  2, "F":  0, "P": -3, "S": -3, "T": -1, "W": -3, "Y": -1, "V":  4}, 
			"L": {"A": -2, "R": -3, "N": -4, "D": -4, "C": -2, "Q": -2, "E": -3, "G": -4, "H": -3, "I":  2, "L":  5, "K": -3, "M":  3, "F":  1, "P": -4, "S": -3, "T": -1, "W": -2, "Y": -1, "V":  1}, 
			"K": {"A": -1, "R":  3, "N":  0, "D": -1, "C": -3, "Q":  2, "E":  1, "G": -2, "H":  0, "I": -3, "L": -3, "K":  6, "M": -2, "F": -4, "P": -1, "S":  0, "T": -1, "W": -3, "Y": -2, "V": -3}, 
			"M": {"A": -1, "R": -2, "N": -2, "D": -4, "C": -2, "Q":  0, "E": -2, "G": -3, "H": -1, "I":  2, "L":  3, "K": -2, "M":  7, "F":  0, "P": -3, "S": -2, "T": -1, "W": -1, "Y":  0, "V":  1}, 
			"F": {"A": -3, "R": -3, "N": -4, "D": -5, "C": -2, "Q": -4, "E": -3, "G": -4, "H": -1, "I":  0, "L":  1, "K": -4, "M":  0, "F":  8, "P": -4, "S": -3, "T": -2, "W":  1, "Y":  4, "V": -1}, 
			"P": {"A": -1, "R": -3, "N": -2, "D": -1, "C": -4, "Q": -1, "E": -1, "G": -2, "H": -2, "I": -3, "L": -4, "K": -1, "M": -3, "F": -4, "P": 10, "S": -1, "T": -1, "W": -4, "Y": -3, "V": -3}, 
			"S": {"A":  1, "R": -1, "N":  1, "D":  0, "C": -1, "Q":  0, "E": -1, "G":  0, "H": -1, "I": -3, "L": -3, "K":  0, "M": -2, "F": -3, "P": -1, "S":  5, "T":  2, "W": -4, "Y": -2, "V": -2}, 
			"T": {"A":  0, "R": -1, "N":  0, "D": -1, "C": -1, "Q": -1, "E": -1, "G": -2, "H": -2, "I": -1, "L": -1, "K": -1, "M": -1, "F": -2, "P": -1, "S":  2, "T":  5, "W": -3, "Y": -2, "V":  0}, 
			"W": {"A": -3, "R": -3, "N": -4, "D": -5, "C": -5, "Q": -1, "E": -3, "G": -3, "H": -3, "I": -3, "L": -2, "K": -3, "M": -1, "F":  1, "P": -4, "S": -4, "T": -4, "W": 15, "Y":  2, "V": -3}, 
			"Y": {"A": -2, "R": -1, "N": -2, "D": -3, "C": -3, "Q": -1, "E": -2, "G": -3, "H":  2, "I": -1, "L": -1, "K": -2, "M":  0, "F":  4, "P": -3, "S": -2, "T": -2, "W":  2, "Y":  8, "V": -1}, 
			"V": {"A":  0, "R": -3, "N": -3, "D": -4, "C": -1, "Q": -3, "E": -3, "G": -4, "H": -4, "I":  4, "L":  1, "K": -3, "M":  1, "F": -1, "P": -3, "S": -2, "T":  0, "W": -3, "Y": -1, "V":  5}}


##########################
#	  Initialization     #
##########################

# Dict with paths in the shape {path_number: [[i_pos,j_pos],"seq_1","seq_2"]}
paths = {}

unfinished_paths = []

max_score = 0
path_index = 0
next_i = 0
next_j = 0

initial_s1 = input("Introduza a 1ª sequencia: ")
initial_s2 = input("Introduza a 2ª sequencia: ")
gap = int(input("Insira o gap: "))

initial_s1_len = len(initial_s1)
initial_s2_len = len(initial_s2)


##########################
#		Functions        #
##########################


# creates a new path with a position and sequences
def create_new_path(i, j, seq_1, seq_2, path_index):
	paths[path_index] = [[i,j],seq_1,seq_2]
	flag_more_paths = 1
	unfinished_paths.append(path_index)
	path_index +=1
	return path_index

# updates the position and sequences of a certain path
def update_path(i, j, seq_1, seq_2):
	paths[current_index] = [[i,j],seq_1,seq_2]
	next_i = i
	next_j = j
	flag_more_paths = 1
	return [next_i, next_j],flag_more_paths


##########################
#		   Code          #
##########################


# Create matrix
F = np.zeros((initial_s1_len+1,initial_s2_len+1), dtype=int)


# Build the matrix with optimal scores for each position
for i in range(1,initial_s1_len+1):
	for j in range(1,initial_s2_len+1):
		value = max(F[i-1,j-1]+blosum50[initial_s1[i-1]][initial_s2[j-1]], F[i-1,j]+gap, F[i,j-1]+gap)
		if value < 0:
			F[i,j] = 0
		else:
			F[i,j] = value
			if value > max_score:
				max_score = value


# Find the positions that match the maximum score
for i in range(1,initial_s1_len+1):
	for j in range(1,initial_s2_len+1):
		if F[i,j] == max_score:
			paths[path_index] = [[i,j],"",""]
			unfinished_paths.append(path_index)
			path_index +=1
	

# Do the traceback for all the paths

while len(unfinished_paths) != 0:

	current_index = unfinished_paths[0]
	i = paths[current_index][0][0]
	j = paths[current_index][0][1]


	while F[i,j] != 0:

		flag_more_paths = 0

		s1 = paths[current_index][1]
		s2 = paths[current_index][2]

		if F[i-1,j-1]+blosum50[initial_s1[i-1]][initial_s2[j-1]] == F[i,j]:
			next_pos, flag_more_paths = update_path(i-1,j-1, initial_s1[i-1] + s1, initial_s2[j-1] + s2)
		
		if F[i-1,j]+gap == F[i,j]:
			if flag_more_paths:
				path_index = create_new_path(i-1,j, initial_s1[i-1] + s1, "-" + s2)
			else:
				next_pos, flag_more_paths = update_path(i-1,j, initial_s1[i-1] + s1, "-" + s2)

		if F[i,j-1]+gap == F[i,j]:
			if flag_more_paths:
				path_index = create_new_path(i, j-1, "-" + s1, initial_s2[j-1] + s2)
			else:
				next_pos, flag_more_paths = update_path(i, j-1, "-" + s1, initial_s2[j-1] + s2)

		i = next_pos[0]
		j = next_pos[1]

	del unfinished_paths[0]


# Print optimal alignments and scores
for path in paths:
	print("\n{:d}.\t{}\n  \t{}\n  Score: {:d}".format(path+1, paths[path][1], paths[path][2], max_score))













