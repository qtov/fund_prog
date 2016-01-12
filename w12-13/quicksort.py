unsorted_list = [5, 6, 7, 2, 3, 4, 1, 0, 23, 41, 21, 6, 5, 4, 2, 3, 3, 4, 1]

def quicksort(lst, lo, hi):
	if (lo < hi):
		p = partition(lst, lo, hi)
		quicksort(lst, lo, p - 1)
		quicksort(lst, p + 1, hi)

def partition(lst, lo, hi):
	pivot = lst[hi]
	i = lo
	for j in range(lo, hi):
		if (lst[j] <= pivot):
			aux = lst[i]
			lst[i] = lst[j]
			lst[j] = aux
			i += 1
	aux = lst[i]
	lst[i] = lst[hi]
	lst[hi] = aux
	return i

def sort(lst):
	quicksort(lst, 0, len(lst) - 1)

print(unsorted_list)

sort(unsorted_list)

print(unsorted_list)
