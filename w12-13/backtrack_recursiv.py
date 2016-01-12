lst = [5, 4, 1, 5, 1, 2, 7, 5, 3, 4, 5, 6]

def backtrack(lst, aux_list, pos, i):
	if (pos < len(lst)):
		if (len(aux_list) == 0):
			aux_list.append(lst[pos])
			print(aux_list)
		else:
			if (i < len(lst) and lst[i] > aux_list[len(aux_list) - 1]):
				aux_list.append(lst[i])
				print(aux_list)
			else:
				aux_list = []
				pos += 1
				i = pos - 1
		backtrack(lst, aux_list, pos, i + 1)

def everybody_do_the_flop(lst):
	backtrack(lst, [], 0, 0)

everybody_do_the_flop(lst)
