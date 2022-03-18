import numpy as np


def post_prob(a, e, S, pos):

	nr_states = len(a)
	seq_size = len(S)

	
	f_0 = 1
	f = np.zeros((nr_states, seq_size))

	b_N = 1
	b = np.zeros((nr_states, seq_size))



	# calculate first column of f based on initial prob
	for i in range(nr_states):
		f[i,0] = e[S[0]][i] * (1/nr_states) * f_0


	# calculate f matrix
	for j in range(1,seq_size):
		letter = S[j]

		for i in range(nr_states):
			# forward algorithm
			lst = []
			for k in range(nr_states):
				lst += [a[k,i]*f[k,j-1]]

			f[i,j] = e[letter][i] * sum(lst)


	# calculate last column of b based on initial prob
	for i in range(nr_states):
		b[i,seq_size-1] = 1


	# calculate b matrix
	for j in range(seq_size-2, -1, -1):
		letter = S[j+1]

		for i in range(nr_states):
			# backward algorithm
			lst = []
			for k in range(nr_states):
				lst += [e[letter][k] * a[i,k] * b[k,j+1]]

			b[i,j] = sum(lst)


	prob = 0
	for i in range(nr_states):
		prob += f[i,seq_size-1]


	post_prob = [0 for i in range(nr_states)]

	print()
	print(b)
	print(f)
	for i in range(nr_states):
		post_prob[i] = (f[i,pos-1] * b[i,pos-1]) / prob
		print("P(π{}={}|{}) = {}".format(pos, i+1, S, post_prob[i]))



