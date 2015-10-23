def is_in_range(_var, start, end):
	if (_var < start or _var > end):
		return (0)
	else:
		return (1)

def is_in_list(_var, _list):
	for elem in _list:
		if (elem == _var):
			return (1)
	return (0)
