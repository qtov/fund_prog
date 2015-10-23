def getTransactions(account):
	return (account['transactions'])

def create_list_index(length):
	index_list = []
	i = 0
	while (i < length):
		index_list.append(i)
		i += 1
	return (index_list)

def print_transaction(transaction):
	print('Ziua = ' + str(transaction['day']) + '; ', end = '')
	print('Suma = ' + str(transaction['amount']) + '; ', end = '')
	print('Tipul = ' + str(transaction['type']) + '.')

def print_transactions_in_order(account, ordered_list, _type):
	for i in ordered_list:
		print_transaction(getTransactions(account)[i])
