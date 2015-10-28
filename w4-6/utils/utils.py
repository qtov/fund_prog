from _globals import *

def _pass(x):
	pass

def add_to_test_array(transaction):
	global TEST_ARRAY
	TEST_ARRAY.append(transaction)

def getTransactions(account):
	return (account['transactions'])

def getDay(transaction):
	return (transaction['day'])

def getAmount(transaction):
	return (transaction['amount'])

def getType(transaction):
	return (transaction['type'])

def getHistory(account):
	return (account['history'])

def create_list_index(length):
	"""
	Creeaza o lista de pozitii in ordine crescatoare.
	De ex: Daca argumentul este 5 se creeaza lista [0, 1, 2, 3, 4]
	"""
	index_list = []
	i = 0
	while (i < length):
		index_list.append(i)
		i += 1
	return (index_list)

def add_to_history(account):
	"""
	Adauga in istoric tranzactia existenta inainte de a fi editata.
	"""
	getHistory(account).append([trans.copy() for trans in getTransactions(account)])

def print_transaction(transaction):
	print('Ziua = ' + str(getDay(transaction)) + '; ', end = '')
	print('Suma = ' + str(getAmount(transaction)) + '; ', end = '')
	print('Tipul = ' + str(getType(transaction)) + '.')

def print_transactions_in_order(account, ordered_list, _type):
	for i in ordered_list:
		print_transaction(getTransactions(account)[i])
