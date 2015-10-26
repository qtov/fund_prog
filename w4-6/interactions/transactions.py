from _globals import *
from utils.utils import *
from UI.validate import *

def add_transaction(_day, _amount, _type, account):
	add_to_history(account)
	getTransactions(account).append({"day": _day, "amount": _amount, "type": _type})

def transaction_exists(_day, _amount, _type, account):
	pos = 0
	for transaction in getTransactions(account):
		if (getDay(transaction) == _day and getAmount(transaction) == _amount \
				and getType(transaction) == _type):
			return (pos)
		pos += 1
	return (-1)

def edit_transaction(transaction_at, _day, _amount, _type, account):
	add_to_history(account)
	getTransactions(account)[transaction_at]['day'] = _day
	getTransactions(account)[transaction_at]['amount'] = _amount
	getTransactions(account)[transaction_at]['type'] = _type

def delete_transaction_type(account, _type):
	deleted = False
	was_deleted = True
	while (was_deleted):
		was_deleted = False;
		for transaction in getTransactions(account):
			if (getType(transaction) == _type):
				if (not deleted):
					add_to_history(account)
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
			if (getDay(transaction) == _day):
				if (not deleted):
					add_to_history(account)
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
			if (getDay(transaction) >= _day1 and \
					getDay(transaction) <= _day2):
				if (not deleted):
					add_to_history(account)
				getTransactions(account).remove(transaction)
				deleted = True
				was_deleted = True
	return (deleted)

def search_transaction_bigger(account, _amount, execute):
	printed = False
	for transaction in getTransactions(account):
		if (getAmount(transaction) > _amount):
			execute(transaction)
			printed = True
	return (printed)

def search_transaction_bigger_before_day(account, _day, _amount, execute):
	printed = False
	for transaction in getTransactions(account):
		if (getDay(transaction) < _day and getAmount(transaction) > _amount):
			execute(transaction)
			printed = True
	return (printed)

def search_transaction_type(account, _type, execute):
	printed = False
	for transaction in getTransactions(account):
		if (getType(transaction) == _type):
			execute(transaction)
			printed = True
	return (printed)

def report_type_amount(account, _type):
	_amount = 0
	for transaction in getTransactions(account):
		if (getType(transaction) == _type):
			_amount += getAmount(transaction)
	return (float("%.2f" % _amount))

def report_balance_date(account, _day):
	balance = 0
	for transaction in getTransactions(account):
		if (getDay(transaction) <= _day):
			if (getType(transaction) == 'iesire'):
				balance -= getAmount(transaction)
			else:
				balance += getAmount(transaction)
	return (float("%.2f" % balance))

def report_order_type_by_amount(account):
	index_list = create_list_index(len(getTransactions(account)))
	ordered = False
	while (not ordered):
		ordered = True
		index = 0
		for index in range(len(index_list) - 1):
			if (getAmount(getTransactions(account)[index_list[index]]) > \
					getAmount(getTransactions(account)[index_list[index + 1]])):
				aux = index_list[index]
				index_list[index] = index_list[index + 1]
				index_list[index + 1] = aux
				ordered = False
	return (index_list)

def filter_del_type(account, _type, execute):
	for transaction in getTransactions(account):
		if (getType(transaction) != _type):
			execute(transaction)

def filter_del_type_rm(account, _type):
	#The same as delete_transaction_type
	was_deleted = True
	deleted = False
	while (was_deleted):
		was_deleted = False
		for transaction in getTransactions(account):
			if (getType(transaction) == _type):
				if (not deleted):
					add_to_history(account)
				deleted = True
				was_deleted = True
	return (deleted)

def filter_smaller_by_type(account, _amount, _type, execute):
	for transaction in getTransactions(account):
		if (getType(transaction) != _type and getAmount(transaction) >= _amount):
			execute(transaction)

def filter_smaller_by_type_rm(account, _amount, _type):
	was_deleted = True
	deleted = False
	while (was_deleted):
		was_deleted = False
		for transaction in getTransactions(account):
			if (getType(transaction) == _type and getAmount(transaction) < _amount):
				if (not deleted):
					add_to_history(account)
				getTransactions(account).remove(transaction)
				was_deleted = True
				deleted = True
	return (deleted)

def undo(account):
	if (len(getHistory(account)) > 0):
		account['transactions'] = getHistory(account)[len(getHistory(account)) - 1]
		getHistory(account).pop()
		return ('Undo successful...')
	else:
		return ('There is nothing to undo.')
