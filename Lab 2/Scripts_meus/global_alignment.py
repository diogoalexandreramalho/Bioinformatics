import numpy as np



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

initial_s1 = input("Introduza a 1ª sequencia: ")
initial_s2 = input("Introduza a 2ª sequencia: ")
match = int(input("Insira o match: "))
mismatch = int(input("Insira o mismatch: "))
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


# Initialize matrix with F(i,0) = -id and F(0,j)=-jd
for i in range(initial_s1_len+1):
	F[i][0] = gap*i

for j in range(initial_s2_len+1):
	F[0][j] = gap*j


# Calculate matrix values
for i in range(1,initial_s1_len+1):
	for j in range(1,initial_s2_len+1):
		if(initial_s1[i-1]==initial_s2[j-1]):
			F[i,j] = max(F[i-1,j-1]+match, F[i-1,j]+gap, F[i,j-1]+gap)
		else:
			F[i,j] = max(F[i-1,j-1]+mismatch, F[i-1,j]+gap, F[i,j-1]+gap)


# Define the value in last column and last row as the start of traceback
paths[path_index] = [[initial_s1_len,initial_s2_len],"",""]
unfinished_paths.append(path_index)
path_index +=1


# Do the traceback for all the paths
while len(unfinished_paths) != 0:

	# Choose next path to trace
	current_index = unfinished_paths[0]
	i = paths[current_index][0][0]
	j = paths[current_index][0][1]


	while (i,j) != (0,0):

		flag_more_paths = 0

		s1 = paths[current_index][1]
		s2 = paths[current_index][2]


		if F[i-1,j-1]+match == F[i,j] and initial_s1[i-1]==initial_s2[j-1]:
			next_pos, flag_more_paths = update_path(i-1,j-1, initial_s1[i-1] + s1, initial_s2[j-1] + s2)

		if F[i-1,j-1]+mismatch == F[i,j] and initial_s1[i-1]!=initial_s2[j-1]:
			if flag_more_paths:
				path_index = create_new_path(i-1,j-1, initial_s1[i-1] + s1, initial_s2[j-1] + s2, path_index)
			else:
				next_pos, flag_more_paths = update_path(i-1,j-1, initial_s1[i-1] + s1, initial_s2[j-1] + s2)
		
		if F[i-1,j]+gap == F[i,j]:
			if flag_more_paths:
				path_index = create_new_path(i-1,j, initial_s1[i-1] + s1, "-" + s2, path_index)
			else:
				next_pos, flag_more_paths = update_path(i-1,j, initial_s1[i-1] + s1, "-" + s2)

		if F[i,j-1]+gap == F[i,j]:
			if flag_more_paths:
				path_index = create_new_path(i, j-1, "-" + s1, initial_s2[j-1] + s2, path_index)
			else:
				next_pos, flag_more_paths = update_path(i, j-1, "-" + s1, initial_s2[j-1] + s2)

		i = next_pos[0]
		j = next_pos[1]


	del unfinished_paths[0]


# Print optimal alignments and scores
for path in paths:
	print("\n{:d}.\t{}\n  \t{}\n  Score: {:d}".format(path+1, paths[path][1], paths[path][2], F[initial_s1_len,initial_s2_len]))

