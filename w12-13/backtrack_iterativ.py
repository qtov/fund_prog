lst = [5, 4, 1, 5, 1, 2, 7, 5, 3, 4, 5, 6]

def backtrack(lst):
	seq = []
	i = 0
	pos = 0
	while (pos < len(lst)):
		if (len(seq) == 0):
			seq.append(lst[pos])
			print(seq)
		else:
			if (i < len(lst) and lst[i] > seq[len(seq) - 1]):
				seq.append(lst[i])
				print(seq)
			else:
				seq = []
				pos += 1
				i = pos - 1
		i += 1

backtrack(lst)
