from viterbi_forward import viterbi_forward
from viterbi_with_log import viterbi_log
from post_prob import post_prob
import numpy as np


algorithm = input("Choose an algorithm:\n\t1 - Viterbi\n\t2 - Viterbi with log\n\t3 - Forward\n\t4 - Posterior probs\nChoice: ")

S = input("Introduce a sequence: ")

# Transition probabilities matrix
a = np.array([[0.6,0.4,0],[0.25,0.5,0.25],[0.25,0.25,0.5]])

# emissions probabilities
e = {"A": [0.4,0.1,0.4], "T": [0.3,0.1,0.3], "C": [0,0.4,0.3], "G": [0.3,0.4,0]}




if algorithm in ["1", "3"]:
	viterbi_forward(a, e, S, algorithm, None, False)

elif algorithm == "4":
	pos = int(input("\nChoose the position that you want the posterior probability: "))
	# gets posterior probabilities
	post_prob(a, e, S, pos)
	# gets state that corresponds to pos in π*
	viterbi_forward(a, e, S, "1", pos, True)

else:
	viterbi_log(a, e, S, algorithm)
