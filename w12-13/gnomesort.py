unsorted_list = [5, 6, 7, 2, 3, 4, 1, 0, 23, 41, 21, 6, 5, 4, 2, 3, 3, 4, 1]

def gnomeSort(lst):
	pos = 1
	while (pos < len(lst)):
		if (lst[pos] >= lst[pos-1]):
			pos += 1
		else:
			aux = lst[pos]
			lst[pos] = lst[pos - 1]
			lst[pos - 1] = aux
			if (pos > 1):
				pos -= 1

print(unsorted_list)

gnomeSort(unsorted_list)

print(unsorted_list)
