from NW_general import NW_general
from MSA import MSA
import copy

algorithm = input("Se pretender o algoritmo NW_general pressione 1\nSe pretender MSA pressione 2\nSelecione: ")
algorithm = int(algorithm)
if algorithm == 1:
	initial_s1 = input("Introduza sequencia na forma GGATCC: ")
	initial_s2 = input("Introduza sequencia na forma GGCCG: ")
	match = input("Introduza match: ")
	mismatch = input("Introduza mismatch: ")
	gap = input("Introduza gap: ")
	alignments, final_score = NW_general(initial_s1,initial_s2,int(match),int(mismatch),int(gap))
	print("Alignments: ")
	print(alignments)
	print("Score: ")
	print(final_score)
elif algorithm == 2:
	sequences = input("Introduza sequencias na forma AACGTC,AGCGCC,CCCGT,ACAT: ")
	sequences = str(sequences).split(',')
	match = input("Introduza match: ")
	mismatch = input("Introduza mismatch: ")
	gap = input("Introduza gap: ")
	sequences_aligned, sum_of_pairs = MSA(sequences,int(match),int(mismatch),int(gap))
	print("Alignments: ")
	print(sequences_aligned)
	print("Sum of pairs: ")
	print(sum_of_pairs)
else:
	print("Tem que introduzir 1 ou 2")







