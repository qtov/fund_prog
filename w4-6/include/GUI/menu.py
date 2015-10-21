#Problema 4: Cont bancar.

from include.interactions.tranzactions import *
from include.GUI.validate import *

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
	if (choice == '1'):
		add_UI_transaction(account)
	elif (choice == '2'):
		edit_UI_transaction(account)

def execute_option_del(account, choice):
	if (choice == '1'):
		delete_UI_transaction_day(account)
	elif (choice == '2'):
		delete_UI_transaction_range(account)
	elif (choice == '3'):
		delete_UI_transaction_type(account)

def execute_x_option(account, option_number, choice):
	if (option_number == 1):
		execute_option_add(account, choice)
	elif (option_number == 2):
		execute_option_del(account, choice)
	elif (option_number == 3):
		pass
	elif (option_number == 4):
		pass
	elif (option_number == 5):
		pass
	elif (option_number == 6):
		pass

def read_x_option(account, show_x_menu, length, option_number):
	show_x_menu()
	opt = [input("Introduceti optiunea: ")]
	until_valid_op(show_x_menu, length, opt)
	execute_x_option(account, option_number, opt[0])

def read_option(account):
	opt = ['0']
	while (opt[0] != '7'):
		show_menu()
		print(account)
		opt = [input("Introduceti optiunea: ")]
		until_valid_op(show_menu, 8, opt) ##CHANGE IT to 7
		if (opt[0] == '1'):
			read_x_option(account, show_x_menu_add, 3, 1)
		elif (opt[0] == '2'):
			read_x_option(account, show_x_menu_del, 4, 2)
		elif (opt[0] == '3'):
			pass
			#read_x_option()
		elif (opt[0] == '4'):
			pass
			#read_x_option()
		elif (opt[0] == '5'):
			pass
			#read_x_option()
		elif (opt[0] == '6'):
			pass
			#read_x_option()
		elif (opt[0] == '7'):
			exit (0)
		else:
			print(account) ##delete it
