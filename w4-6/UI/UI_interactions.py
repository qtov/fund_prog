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
				print("Ziua invalida.")	
			else:
				break
		except ValueError:
			print("Ziua invalida, introduceti un intreg.")
	return (_day)

def read_day():
	while True:
		_day = input("Introduceti ziua: ")
		try:
			_day = int(_day)
			if (not is_in_range(_day, 0, VALID_DAY)):
				print("Ziua invalida.")
			else:
				break
		except ValueError:
			print("Ziua invalida, introduceti un intreg.")
	return (_day)

def read_amount():
	while True:
		_amount = input("Introduceti suma: ")
		try:
			_amount = float(_amount)
			if (not is_in_range(_amount, 0, VALID_AMOUNT)):
				print("Suma invalida, nu se inscrie in interval.")
			else:
				break
		except ValueError:
			print("Suma invalida, introduceti un numar.")
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
	transaction_at = transaction_exists(_day, _amount, _type, account)
	if (transaction_at != -1):
		print('Actualizare tranzactie...')
		_day = read_day()
		_amount = read_amount()
		_type = read_type()
		edit_transaction(transaction_at, _day, _amount, _type, account)
	else:
		print('Tranzactie inexistenta.')

def delete_UI_transaction_day(account):
	_day = read_day()
	deleted = delete_transaction_day(account, _day)
	if (not deleted):
		print('Nu s-a efectuat nici o stergere.')

def delete_UI_transaction_range(account):
	_day1 = read_day_range('start')
	_day2 = read_day_range('end')
	if (_day1 > _day2):
		print('Perioada invalida.')
	else:
		deleted = delete_transaction_range(account, _day1, _day2)
		if (not deleted):
			print('Nu s-a efectuat nici o stergere.')

def delete_UI_transaction_type(account):
	_type = read_type()
	deleted = delete_transaction_type(account, _type)
	if (not deleted):
		print('Nu s-a efectuat nici o stergere.')

def search_UI_transaction_bigger(account):
	_amount = read_amount()
	found = search_transaction_bigger(account, _amount)
	if (not found):
		print("Nu exista nici o tranzactie cu suma mai mare de %f." % (_amount))

def search_UI_transaction_bigger_before_day(account):
	_day = read_day()
	_amount = read_amount()
	found = search_transaction_bigger_before_day(account, _day, _amount)
	if (not found):
		print('Nu exista nici o tranzactie efectuata inainte de ziua', \
				"%d cu suma mai mare de %f" % (_day, _amount))

def search_UI_transaction_type(account):
	_type = read_type()
	found = search_transaction_type(account, _type)
	if (not found):
		print("Nu exista nici o tranzactie de tipul %s." % (_type))

def report_UI_type_amount(account):
	_type = read_type()
	print(report_type_amount(account, _type))

def report_UI_balance_date(account):
	_day = read_day()
	print(report_balance_date(account, _day))
