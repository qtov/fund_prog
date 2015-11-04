from _globals import *
from utils.utils import *
from interactions.transactions import *

def read_day_range(where):
	"""Citeste ziua de inceput sau ziua de final."""
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
	"""Citeste ziua si o valideaza."""
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
	"""Citeste suma si o valideaza."""
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
	"""Citeste tipul si il valideaza."""
	while True:
		_type = input("Introduceti tipul: ")
		if (is_in_list(_type, VALID_TYPES)):
			return (_type)
		else:
			print("Tipul este invalid.")

def add_UI_transaction(account):
	"""Citeste tranzactia de adaugat."""
	_day = read_day()
	_amount = read_amount()
	_type = read_type()
	add_transaction(_day, _amount, _type, account)

def edit_UI_transaction(account):
	"""Citeste tranzactia de actualizat."""
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
		print('Tranzactie actualizata.')
	else:
		print('Tranzactie inexistenta.')

def delete_UI_transaction_day(account):
	"""Citeste ziua tranzactiilor de sters."""
	_day = read_day()
	deleted = delete_transaction_day(account, _day)
	if (not deleted):
		print('Nu s-a efectuat nici o stergere.')
	else:
		print('Stergere finalizata.')

def delete_UI_transaction_range(account):
	"""Citeste zilele tranzactiilor de sters. (Un interval)"""
	_day1 = read_day_range('start')
	_day2 = read_day_range('end')
	if (_day1 > _day2):
		print('Perioada invalida.')
	else:
		deleted = delete_transaction_range(account, _day1, _day2)
		if (not deleted):
			print('Nu s-a efectuat nici o stergere.')
		else:
			print('Stergere finalizata.')

def delete_UI_transaction_type(account):
	"""Citeste tipul tranzactiilor de sters."""
	_type = read_type()
	deleted = delete_transaction_type(account, _type)
	if (not deleted):
		print('Nu s-a efectuat nici o stergere.')
	else:
		print('Stergere finalizata.')

def search_UI_transaction_bigger(account):
	"""Citeste suma si afiseaza tranzactiile mai mari decat suma data."""
	_amount = read_amount()
	found = search_transaction_bigger(account, _amount, print_transaction)
	if (not found):
		print("Nu exista nici o tranzactie cu suma mai mare de %f." % (_amount))

def search_UI_transaction_bigger_before_day(account):
	"""
	Citeste ziua, suma si afiseaza tranzactiile mai mari decat suma data 
	inainte de ziua data.
	"""
	_day = read_day()
	_amount = read_amount()
	found = search_transaction_bigger_before_day(account, _day, _amount, print_transaction)
	if (not found):
		print('Nu exista nici o tranzactie efectuata inainte de ziua', \
				"%d cu suma mai mare de %f" % (_day, _amount))

def search_UI_transaction_type(account):
	"""Cisteste tipul si afiseaza tranzactiile de tipul dat."""
	_type = read_type()
	found = search_transaction_type(account, _type, print_transaction)
	if (not found):
		print("Nu exista nici o tranzactie de tipul %s." % (_type))

def report_UI_type_amount(account):
	"""Citeste tipul tranzactiei pentru care se calculeaza suma."""
	_type = read_type()
	print("Suma tranzactiilor de tipul %s este: " % (report_type_amount(account, _type)))

def report_UI_balance_date(account):
	"""Citeste ziua tranzactiei pentru care se calculeaza suma."""
	_day = read_day()
	print("Soldul contului in ziua %d este: %.2f" % (_day, 
	report_balance_date(account, _day)))

def report_UI_order_type_by_amount(account):
	"""Citeste tipul tranzactiilor care se ordoneaza dupa suma."""
	_type = read_type()
	ordered_index_list = report_order_type_by_amount(account)
	print_transactions_in_order(account, ordered_index_list, _type)

def filter_UI_del_type(account):
	"""Citeste tipul tranzactiilor care nu se afiseaza."""
	_type = read_type()
	filter_del_type(account, _type, print_transaction)

def filter_UI_del_type_rm(account):
	"""Citeste tipul tranzactiilor de sters."""
	_type = read_type()
	filtered = delete_transaction_type(account, _type)
	if (not filtered):
		print('Nu s-a efectuat nici o filtrare.')
	else:
		print('Filtrare finalizata.')

def filter_UI_smaller_by_type(account):
	"""
	Citeste tipul, suma tranzactiilor de afisat cu tipul diferit si suma mai mare sau egala.
	"""
	_amount = read_amount()
	_type = read_type()
	filter_smaller_by_type(account, _amount, _type, print_transaction)

def filter_UI_smaller_by_type_rm(account):
	"""
	Citeste tipul, suma tranzactiilor de sters de tipul dat cu suma mai mica decat suma data.
	"""
	_amount = read_amount()
	_type = read_type()
	filtered = filter_smaller_by_type_rm(account, _amount, _type)
	if (not filtered):
		print('Nu s-a efectual nici o filtrare.')
	else:
		print('Filtrare finalizata.')
