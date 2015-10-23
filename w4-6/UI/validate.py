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

def is_valid_option(n, to_what):
	i = 0
	if (len(n) == 0):
		return False
	while (i < len(n)):
		if (not (n[i] >= '0' and n[i] <= '9')):
			return False
		i += 1
	if (int(n) >= 1 and int(n) <= to_what):
		return True
	else:
		return False

def until_valid_op(show_menu, length, n):
	while (not is_valid_option(n[0], length)):
		print('Optiune invalida!!!')
		show_menu()
		n[0] = input('Introduceti optiunea: ')

def until_valid_int(length, n, _type):
	while (not is_valid_option(n[0], length)):
		print(_type + ' invalida!!!')
		n[0] = input('Reintroduceti ' + _type + ': ')

def is_valid_float(s, to_what):
	i = 0
	dot_count = 0
	while (i < len(s)):
		if (not (s[i] >= '0' and s[i] <= '9') and s[i] != '.'):
			return False
		elif (s[i] == '.'):
			dot_count += 1
		i += 1
	if (s == ''):
		return False
	if (dot_count > 1 or float(s) > to_what):
		return False
	return True

def until_valid_float(length, n, _type):
	while (not is_valid_float(n[0], length)):
		print(_type + ' invalida!!!')
		n[0] = input("Reintroduceti " + _type + ': ')

def is_valid_type(lst, _type):
	for i in lst:
		if (_type == i):
			return True
	return False

def until_valid_type(lst, _type, _type_str):
	while (not is_valid_type(lst, _type[0])):
		print(_type_str + ' invalid!!!')
		_type[0] = input("Reintroduceti " + _type_str + ': ')
