# Worst case performance - О(n^2)	#
# Best case performance - О(n^2)	#
# Average case performance - О(n^2)	#

unsorted_list = [5, 6, 7, 2, 3, 4, 1, 0, 23, 41, 21, 6, 5, 4, 2, 3, 3, 4, 1]

def selection_sort(lst):
	sorted_items = 0;
	while (sorted_items < len(lst)):
		lstmin = lst[sorted_items];
		pos = i = sorted_items
		while (i < len(lst)):
			if (lst[i] < lstmin):
				lstmin = lst[i]
				pos = i
			i += 1
		aux = lst[sorted_items]
		lst[sorted_items] = lst[pos]
		lst[pos] = aux
		sorted_items += 1

print(unsorted_list)

selection_sort(unsorted_list)

print(unsorted_list)


