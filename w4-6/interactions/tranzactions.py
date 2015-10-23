from UI.validate import *

def add_transaction(_day, _amount, _type, account):
	if (_type == 'iesire'):
		account["current"] -= _amount
	else:
		account['current'] += _amount
	account["transactions"].append({"day": _day, "amount": _amount, "type": _type})

def transaction_exists(_day, _amount, _type, account):
	pos = 0
	for elem in account["transactions"]:
		if (elem["day"] == _day and elem["amount"] == _amount and elem["type"] == _type):
			return pos
		pos += 1
	raise UserWarning

def edit_transaction(transaction_at, _day, _amount, _type, account):
	account['transactions'][transaction_at]['day'] = _day
	account['transactions'][transaction_at]['amount'] = _amount
	account['transactions'][transaction_at]['type'] = _type

def delete_transaction_type(account, _type):
	deleted = 0
	ok = 1
	while (ok == 1):
		ok = 0;
		for tran in account['transactions']:
			if (tran['type'] == _type):
				if (tran['type'] == 'iesire'):
					tran['amount'] *= -1
				account['current'] -= tran['amount']
				account['transactions'].remove(tran)
				deleted = 1
				ok = 1
	if (deleted == 0):
		raise UserWarning;

def delete_transaction_day(account, _day):
	deleted = 0
	ok = 1
	while (ok == 1):
		ok = 0;
		for tran in account['transactions']:
			if (tran['day'] == int(_day)):
				if (tran['type'] == 'iesire'):
					tran['amount'] *= -1
				account['current'] -= tran['amount']
				account['transactions'].remove(tran)
				deleted = 1
				ok = 1
	if (deleted == 0):
		raise UserWarning;

def delete_transaction_range(account, _day1, _day2):
	ok = 1
	deleted = 0
	while (ok == 1):
		ok = 0
		for tran in account['transactions']:
			if (tran['day'] >= int(_day1) and tran['day'] <= int(_day2)):
				if (tran['type'] == 'iesire'):
					tran['amount'] *= -1
				account['current'] -= tran['amount']
				account['transactions'].remove(tran)
				deleted = 1
				ok = 1
	if (deleted == 0):
		raise UserWarning;
