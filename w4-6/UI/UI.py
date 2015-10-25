#Problema 4: Cont bancar.

from interactions.tranzactions import *
from UI.validate import *
from UI.UI_interactions import *

def _read_option(opt_count, show_menu):
	while True:
		opt = input("Introduceti optiunea: ")
		try:
			opt = int(opt)
			if (not is_in_range(opt, 1, opt_count)):
				show_menu()
				print('Optiune invalida.')
			else:
				break
		except ValueError:
			show_menu()
			print('Optiune invalida.')
	if (opt == opt_count):
		return (-1)
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

def show_x_menu_search():
	print("	1. Tipareste tranzactiile cu sume mai mari decat o suma data.")
	print("	2. Tipareste toate tranzactiile efectuate inainte cu " + \
			"o zi si mai mari decat o suma.")
	print("	3. Tipareste tranzactiile de un anumit tip.")
	print("	4. Inapoi.")

def show_x_menu_report():
	print("	1. Suma totala a tranzactiilor de un anumit tip.")
	print("	2. Soldul contului la o data specificata.")
	print("	3. Tipareste toate tranzactiile de un anumit tip ordonat dupa suma.")
	print("	4. Inapoi.")

def show_x_menu_filter():
	print("	1. Elimina toate tranzactiile de un tip.")
	print("	2. Elimina toate tranzactiile mai mici de o suma data care " + \
			"au tipul specificat.")
	print("	3. Inapoi.")

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

def execute_option_find(account, choice):
	if (choice == 1):
		search_UI_transaction_bigger(account)
	elif (choice == 2):
		search_UI_transaction_bigger_before_day(account)
	elif (choice == 3):
		search_UI_transaction_type(account)

def execute_option_report(account, choice):
	if (choice == 1):
		report_UI_type_amount(account)
	elif (choice == 2):
		report_UI_balance_date(account)
	elif (choice == 3):
		report_UI_order_type_by_amount(account)

def execute_option_filter(account, choice):
	if (choice == 1):
		filter_UI_del_type(account)
	elif (choice == 2):
		filter_UI_smaller_by_type(account)

def execute_x_option(account, menu_number, choice):
	if (menu_number == 1):
		execute_option_add(account, choice)
	elif (menu_number == 2):
		execute_option_del(account, choice)
	elif (menu_number == 3):
		execute_option_find(account, choice)
	elif (menu_number == 4):
		execute_option_report(account, choice)
	elif (menu_number == 5):
		execute_option_filter(account, choice)
	if (choice != -1):
		input('Press Enter to continue...') #Dunno about it... is it good?!

def read_x_option(account, show_x_menu, number_of_suboptions, menu_number):
	show_x_menu()
	opt = _read_option(number_of_suboptions, show_x_menu)
	execute_x_option(account, menu_number, opt)

def read_option(account):
	opt = 0
	while (opt != 7):
		show_menu()
		print(account) #The state of the account... Groar!!
		opt = _read_option(7, show_menu)
		"""
		" The 3rd argument from read_x_option is the number
		" of suboptions the option has.
		"""
		if (opt == 1):
			read_x_option(account, show_x_menu_add, 3, opt)
		elif (opt == 2):
			read_x_option(account, show_x_menu_del, 4, opt)
		elif (opt == 3):
			read_x_option(account, show_x_menu_search, 4, opt)
		elif (opt == 4):
			read_x_option(account, show_x_menu_report, 4, opt)
		elif (opt == 5):
			read_x_option(account, show_x_menu_filter, 3, opt)
		elif (opt == 6):
			print(undo(account))
