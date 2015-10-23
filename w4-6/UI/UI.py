#Problema 4: Cont bancar.

from interactions.tranzactions import *
from UI.validate import *
from UI.UI_interactions import *

def _read_option(opt_count):
	while True:
		opt = input("Introduceti optiunea: ")
		try:
			opt = int(opt)
			if (not is_in_range(opt, 1, opt_count)):
				raise UserWarning
			break
		except ValueError:
			print('Optiune invalida.')
		except UserWarning:
			print('Optiune invalida.')
	return (opt)

def show_menu():
	print("1. Adaugare de noi tranzactii.")
	print("2. Stergere.")
	print("3. Cautari.")
	print("4. Rapoarte.")
	print("5. Filtrare.")
	print("6. Undo.")
	print("7. Iesire.")

def show_x_menu_add():
	print("	1. Adauga tranzactie.")
	print("	2. Actualizare tranzactie.")
	print("	3. Inapoi.")

def show_x_menu_del():
	print("	1. Sterge toate tranzactiile de la ziua specificata.")
	print("	2. Sterge tranzactiile dintr-o perioada data.")
	print("	3. Sterge toate tranzactiile de un anumit tip.")
	print("	4. Inapoi.")

def execute_option_add(account, choice):
	if (choice == 1):
		add_UI_transaction(account)
	elif (choice == 2):
		edit_UI_transaction(account)

def execute_option_del(account, choice):
	if (choice == 1):
		delete_UI_transaction_day(account)
	elif (choice == 2):
		delete_UI_transaction_range(account)
	elif (choice == 3):
		delete_UI_transaction_type(account)

def execute_x_option(account, menu_number, choice):
	if (menu_number == 1):
		execute_option_add(account, choice)
	elif (menu_number == 2):
		execute_option_del(account, choice)
	elif (menu_number == 3):
		pass
	elif (menu_number == 4):
		pass
	elif (menu_number == 5):
		pass
	elif (menu_number == 6):
		pass

def read_x_option(account, show_x_menu, length, menu_number):
	show_x_menu()
	opt = _read_option(length)
	execute_x_option(account, menu_number, opt)

def read_option(account):
	while True:
		show_menu()
		print(account)
		opt = _read_option(7)
		if (opt == 1):
			read_x_option(account, show_x_menu_add, 3, opt)
		elif (opt == 2):
			read_x_option(account, show_x_menu_del, 4, opt)
		elif (opt == 3):
			pass
			#read_x_option()
		elif (opt == 4):
			pass
			#read_x_option()
		elif (opt == 5):
			pass
			#read_x_option()
		elif (opt == 6):
			pass
			#read_x_option()
		elif (opt == 7):
			exit (0)
