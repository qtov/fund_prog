from UI.UI import *
from interactions.tranzactions import *

def main():
	account = {"transactions": [], "history": []}
	read_option(account)

if (__name__ == '__main__'):
	test_transaction_exists()
	test_edit_transaction()
	main()
