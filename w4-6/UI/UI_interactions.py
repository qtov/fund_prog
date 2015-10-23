from interactions.tranzactions import *
from _globals import *

def read_day_range(where):
	while True:
		if (where == 'start'):
			_day = input("Introduceti ziua de inceput: ")
		elif (where == 'end'):
			_day = input("Introduceti ziua de sfarsit: ")
		else:
			raise NameError
		try:
			_day = int(_day)
			if (not is_in_range(_day, 0, VALID_DAY)):
				raise UserWarning
			break
		except ValueError:
			print("Ziua invalida, introduceti un intreg.")
		except UserWarning:
			print("Ziua invalida.")	
	return (_day)

def read_day():
	while True:
		_day = input("Introduceti ziua: ")
		try:
			_day = int(_day)
			if (not is_in_range(_day, 0, VALID_DAY)):
				raise UserWarning
			break
		except ValueError:
			print("Ziua invalida, introduceti un intreg.")
		except UserWarning:
			print("Ziua invalida.")
	return (_day)

def read_amount():
	while True:
		_amount = input("Introduceti suma: ")
		try:
			_amount = float(_amount)
			if (not is_in_range(_amount, 0, VALID_AMOUNT)):
				raise UserWarning
			break
		except ValueError:
			print("Suma invalida, introduceti un numar.")
		except UserWarning:
			print("Suma invalida, nu se inscrie in interval.")
	return (_amount)

def read_type():
	while True:
		_type = input("Introduceti tipul: ")
		if (is_in_list(_type, VALID_TYPES)):
			return (_type)
		else:
			print("Tipul este invalid.")

def add_UI_transaction(account):
	_day = read_day()
	_amount = read_amount()
	_type = read_type()
	add_transaction(_day, _amount, _type, account)

def edit_UI_transaction(account):
	_day = read_day()
	_amount = read_amount()
	_type = read_type()
	try:
		transaction_at = transaction_exists(_day, _amount, _type, account)
		print('Actualizare tranzactie...')
		_day = read_day()
		_amount = read_amount()
		_type = read_type()
		edit_transaction(transaction_at, _day, _amount, _type, account)
	except UserWarning:
		print('Tranzactie inexistenta.')

def delete_UI_transaction_day(account):
	_day = read_day()
	try:
		delete_transaction_day(account, _day)
	except UserWarning:
		print('Nu s-a efectuat nici o stergere.')

def delete_UI_transaction_range(account):
	_day1 = read_day_range('start')
	_day2 = read_day_range('end')
	if (_day1 > _day2):
		print('Perioada invalida.')
	else:
		try:
			delete_transaction_range(account, _day1, _day2)
		except UserWarning:
			print('Nu s-a efectuat nici o stergere.')

def delete_UI_transaction_type(account):
	_type = read_type()
	try:
		delete_transaction_type(account, _type)
	except UserWarning:
		print('Nu s-a efectuat nici o stergere.')
