from UI.validate import *

def add_transaction(_day, _amount, _type, account):
	account["transactions"].append({"day": _day, "amount": _amount, "type": _type})

def transaction_exists(_day, _amount, _type, account):
	pos = 0
	for elem in account["transactions"]:
		if (elem["day"] == _day and elem["amount"] == _amount and elem["type"] == _type):
			return pos
		pos += 1
	return (-1)

def edit_transaction(transaction_at, _day, _amount, _type, account):
	account['transactions'][transaction_at]['day'] = _day
	account['transactions'][transaction_at]['amount'] = _amount
	account['transactions'][transaction_at]['type'] = _type

def delete_transaction_type(account, _type):
	deleted = False
	was_deleted = True
	while (was_deleted):
		was_deleted = False;
		for tran in account['transactions']:
			if (tran['type'] == _type):
				account['transactions'].remove(tran)
				deleted = True
				was_deleted = True
	return (deleted)

def delete_transaction_day(account, _day):
	deleted = False
	was_deleted = True
	while (was_deleted):
		was_deleted = False;
		for tran in account['transactions']:
			if (tran['day'] == _day):
				account['transactions'].remove(tran)
				deleted = True
				was_deleted = True
	return (deleted)

def delete_transaction_range(account, _day1, _day2):
	was_deleted = True
	deleted = False
	while (was_deleted):
		was_deleted = False
		for tran in account['transactions']:
			if (tran['day'] >= _day1 and tran['day'] <= _day2):
				account['transactions'].remove(tran)
				deleted = True
				was_deleted = True
	return (deleted)

def print_transaction(transaction):
	print('Ziua = ' + str(transaction['day']) + '; ', end = '')
	print('Suma = ' + str(transaction['amount']) + '; ', end = '')
	print('Tipul = ' + transaction['type'] + '.')

def search_transaction_bigger(account, _amount):
	printed = False
	for transaction in account['transactions']:
		if (transaction['amount'] > _amount):
			print_transaction(transaction)
			printed = True
	return (printed)

def search_transaction_bigger_before_day(account, _day, _amount):
	printed = False
	for transaction in account['transactions']:
		if (transaction['day'] < _day and transaction['amount'] > _amount):
			print_transaction(transaction)
			printed = True
	return (printed)

def search_transaction_type(account, _type):
	printed = False
	for transaction in account['transactions']:
		if (transaction['type'] == _type):
			print_transaction(transaction)
			printed = True
	return (printed)

def report_type_amount(account, _type):
	_amount = 0
	for transaction in account['transactions']:
		if (transaction['type'] == _type):
			_amount += transaction['amount']
	return (_amount)

def report_balance_date(account, _day):
	balance = 0
	for transaction in account['transactions']:
		if (transaction['day'] <= _day):
			if (transaction['type'] == 'iesire'):
				balance -= transaction['amount']
			else:
				balance += transaction['amount']
	return (balance)
