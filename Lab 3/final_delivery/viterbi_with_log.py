import numpy as np
import math


def viterbi_log(a, e_probs, S, viterbi):

	nr_states = len(a)
	seq_size = len(S)

	# v matrix
	v_0 = 1
	v = np.zeros((nr_states, seq_size))
	ptrs = np.zeros((nr_states, seq_size))


	#----------------------------------------
	#
	#			Functions
	#
	#----------------------------------------

	# builds the path that led to the highest probability
	def get_best_path(v, seq_size, nr_states):
		path = ""

		j = seq_size-1
		max_v = -math.inf
		final_state = 0

		# gets last state associated to highest probability
		for i in range(nr_states):
			if v[i,j] > max_v:
				max_v = v[i,j]
				final_state = i

		path += str(final_state+1)

		state = final_state

		# gets sequence of states that led to the highest prob
		for j in range(j, 0, -1):
			state = int(ptrs[state,j])
			path = str(state+1) + path

		return path


	#----------------------------------------
	#
	#				Code
	#
	#----------------------------------------


	# calculate first column of v based on initial prob
	for i in range(3):
		if e_probs[S[0]][i] == 0:
			v[i,0] = -math.inf 
		else:
			v[i,0] = math.log(e_probs[S[0]][i]) + math.log(1/3) + v_0

	# calculate v matrix
	for j in range(1, seq_size):
		letter = S[j]

		for i in range(nr_states):

			max_a_v = -math.inf

			# find max a_v
			for k in range(nr_states):
				if a[k,i] != 0 and math.log(a[k,i]) + v[k,j-1] > max_a_v:
					max_a_v = math.log(a[k,i]) + v[k,j-1]
					previous_state = k

			# store previous state in ptrs matrix
			ptrs[i,j] = previous_state

			if e_probs[letter][i] == 0:
				e = -math.inf
				ptrs[i,j] = -math.inf
			else:
				e = math.log(e_probs[letter][i])

			v[i,j] = e + max_a_v
		

	path = get_best_path(v, seq_size, nr_states)
	print("Path: {}".format(path))






