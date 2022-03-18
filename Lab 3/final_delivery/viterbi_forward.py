import numpy as np
import math



def viterbi_forward(a, e, S, viterbi, pos, post_prob):
	
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


	# get prob of sequence based on sum of values in last column of v
	def calculate_prob(v, nr_states, seq_size):
		prob = 0
		for i in range(nr_states):
			prob += v[i,seq_size-1]
		return prob



	#----------------------------------------
	#
	#				Code
	#
	#----------------------------------------

	# calculate first column of v based on initial prob
	for i in range(nr_states):
		v[i,0] = e[S[0]][i] * (1/nr_states) * v_0

	# calculate v matrix
	for j in range(1,seq_size):
		letter = S[j]

		for i in range(nr_states):
			if viterbi == "1":
				max_a_v = -math.inf

				# find max a_v
				for k in range(nr_states):
					if a[k,i]*v[k,j-1] > max_a_v:
						max_a_v = a[k,i]*v[k,j-1]
						previous_state = k

				# store previous state in ptrs matrix
				ptrs[i,j] = previous_state

				v[i,j] = e[letter][i] * max_a_v

			# forward algorithm
			else:
				lst = []
				for k in range(nr_states):
					lst += [a[k,i]*v[k,j-1]]
				v[i,j] = e[letter][i] * sum(lst)


	if viterbi == "1":
		path = get_best_path(v, seq_size, nr_states)
		
		if not post_prob:
			print("Path: {}".format(path))
		else:
			print("State in position {} in π* -> {}".format(pos, path[pos-1]))


	else:
		prob = calculate_prob(v, nr_states, seq_size)
		print("Prob: {}".format(prob))






