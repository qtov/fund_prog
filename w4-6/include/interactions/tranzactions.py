from include.GUI.validate import *

def add_transaction(_day, _amount, _type, account):
	if (_type == 'iesire'):
		account["current"] -= _amount
	else:
		account['current'] += _amount
	account["transactions"].append({"day": _day, "amount": _amount, "type": _type})

def edit_transaction(_day, _amount, _type, account):
	edited = 0
	for elem in account["transactions"]:
		if (elem["day"] == _day and elem["amount"] == _amount and elem["type"] == _type):
			print('Actualizare tranzactie...')
			_day = [input("Introduceti ziua: ")]
			until_valid_val(31, _day, 'ziua')
			_amount = [input("Introduceti suma: ")]
			until_valid_float(10000, _amount, 'suma')
			_type = [input("Introduceti tipul: ")]
			until_valid_type(['intrare', 'iesire'], _type, 'tipul')
			elem['day'] = int(_day[0])
			elem['_amount'] = float(_amount[0])
			elem['_type'] = _type[0]
			edited = 1
	if (edited == 1):
		print('Actualizare efectuata.')
	else:
		print('Tranzactia nu exista.')

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
		print('Nu s-a gasit nici o tranzactie de tipul specificat.')
	else:
		print('Stergere efectuata.')

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
		print('Nu s-a gasit nici o tranzactie la ziua specificata.')
	else:
		print('Stergere efectuata.')

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
		print('Nu s-a gasit nici o tranzactie in intervalul specificat.')
	else:
		print('Stergere efectuata.')

def add_UI_transaction(account):
	_day = [input("Introduceti ziua: ")]
	until_valid_val(31, _day, 'ziua')
	_amount = [input("Introduceti suma: ")]
	until_valid_float(10000, _amount, 'suma')
	_type = [input("Introduceti tipul: ")]
	until_valid_type(['intrare', 'iesire'], _type, 'tipul')
	add_transaction(int(_day[0]), float(_amount[0]), _type[0], account)

def edit_UI_transaction(account):
	_day = [input("Introduceti ziua: ")]
	until_valid_val(31, _day, 'ziua')
	_amount = [input("Introduceti suma: ")]
	until_valid_float(10000, _amount, 'suma')
	_type = [input("Introduceti tipul: ")]
	until_valid_type(['intrare', 'iesire'], _type, 'tipul')
	edit_transaction(int(_day[0]), float(_amount[0]), _type[0], account)

def delete_UI_transaction_day(account):
	_day = [input("Introduceti ziua: ")]
	until_valid_val(31, _day, 'ziua')
	delete_transaction_day(account, _day[0])

def delete_UI_transaction_range(account):
	_day1 = [input("Introduceti ziua de inceput: ")]
	until_valid_val(31, _day1, 'ziua')
	_day2 = [input("Introduceti ziua de sfarsit: ")]
	until_valid_val(31, _day2, 'ziua')
	if (_day1 > _day2):
		print('Perioada invalida.')
	else:
		delete_transaction_range(account, _day1[0], _day2[0])

def delete_UI_transaction_type(account):
	_type = [input("Introduceti tipul: ")]
	until_valid_type(['intrare', 'iesire'], _type, 'tipul')
	delete_transaction_type(account, _type[0])
