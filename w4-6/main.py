from utils.utils import *
from utils.tests import *
from UI.UI import *

def test_all():
	test_transaction_exists()
	test_edit_transaction()
	test_delete_transaction_type()
	test_delete_transaction_day()
	test_delete_transaction_range()
	test_search_transaction_bigger()
	test_search_transaction_bigger_before_day()
	test_search_transaction_type()
	test_report_type_amount()
	test_report_balance_date()
	test_report_order_type_by_amount()
	test_filter_del_type()
	test_filter_smaller_by_type()
	test_undo()

def main():
	account = {"transactions": [], "history": []}
	read_option(account)

if (__name__ == '__main__'):
	test_all()
	main()
