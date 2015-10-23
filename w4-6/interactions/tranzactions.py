from UI.validate import *
from utils.utils import *

def add_transaction(_day, _amount, _type, account):
	getTransactions(account).append({"day": _day, "amount": _amount, "type": _type})

def transaction_exists(_day, _amount, _type, account):
	pos = 0
	for transaction in getTransactions(account):
		if (transaction["day"] == _day and transaction["amount"] == _amount \
				and transaction["type"] == _type):
			return pos
		pos += 1
	return (-1)

def edit_transaction(transaction_at, _day, _amount, _type, account):
	getTransactions(account)[transaction_at]['day'] = _day
	getTransactions(account)[transaction_at]['amount'] = _amount
	getTransactions(account)[transaction_at]['type'] = _type

def delete_transaction_type(account, _type):
	deleted = False
	was_deleted = True
	while (was_deleted):
		was_deleted = False;
		for transaction in getTransactions(account):
			if (transaction['type'] == _type):
				getTransactions(account).remove(transaction)
				deleted = True
				was_deleted = True
	return (deleted)

def delete_transaction_day(account, _day):
	deleted = False
	was_deleted = True
	while (was_deleted):
		was_deleted = False;
		for transaction in getTransactions(account):
			if (transaction['day'] == _day):
				getTransactions(account).remove(transaction)
				deleted = True
				was_deleted = True
	return (deleted)

def delete_transaction_range(account, _day1, _day2):
	was_deleted = True
	deleted = False
	while (was_deleted):
		was_deleted = False
		for transaction in getTransactions(account):
			if (transaction['day'] >= _day1 and \
					transaction['day'] <= _day2):
				getTransactions(account).remove(transaction)
				deleted = True
				was_deleted = True
	return (deleted)

def search_transaction_bigger(account, _amount):
	printed = False
	for transaction in getTransactions(account):
		if (transaction['amount'] > _amount):
			print_transaction(transaction)
			printed = True
	return (printed)

def search_transaction_bigger_before_day(account, _day, _amount):
	printed = False
	for transaction in getTransactions(account):
		if (transaction['day'] < _day and transaction['amount'] > _amount):
			print_transaction(transaction)
			printed = True
	return (printed)

def search_transaction_type(account, _type):
	printed = False
	for transaction in getTransactions(account):
		if (transaction['type'] == _type):
			print_transaction(transaction)
			printed = True
	return (printed)

def report_type_amount(account, _type):
	_amount = 0
	for transaction in getTransactions(account):
		if (transaction['type'] == _type):
			_amount += transaction['amount']
	return (_amount)

def report_balance_date(account, _day):
	balance = 0
	for transaction in getTransactions(account):
		if (transaction['day'] <= _day):
			if (transaction['type'] == 'iesire'):
				balance -= transaction['amount']
			else:
				balance += transaction['amount']
	return (balance)

def report_order_type_by_amount(account):
	index_list = create_list_index(len(getTransactions(account)))
	ordered = False
	while (not ordered):
		ordered = True
		index = 0
		for index in range(len(index_list) - 1):
			if (getTransactions(account)[index_list[index]]['amount'] > \
					getTransactions(account)[index_list[index + 1]]['amount']):
				aux = index_list[index]
				index_list[index] = index_list[index + 1]
				index_list[index + 1] = aux
				ordered = False
	return (index_list)
