from utils.utils import _pass
from interactions.transactions import *

def test_transaction_exists():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}]}
	assert(transaction_exists(2, 2, 'iesire', account) == 2)
	assert(transaction_exists(2, 14, 'intrare', account) == -1)
	assert(transaction_exists(1, 42.21, 'iesire', account) == 5)
	assert(transaction_exists(1, 1, 'iesire', account) == -1)
	assert(transaction_exists(1, 1, 'intrare', account) == 0)

def test_edit_transaction():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	edit_transaction(0, 2, 2, 'intrare', account)
	assert(account['transactions'] == [{'day': 2, 'amount': 2.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}])
	edit_transaction(4, 6, 5.1, 'intrare', account)
	assert(account['transactions'] == [{'day': 2, 'amount': 2.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 6, 'amount': 5.1, 'type': 'intrare'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}])

def test_delete_transaction_type():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	delete_transaction_type(account, 'intrare')
	assert(account['transactions'] == [{'day': 2, 'amount': 2.0, 'type': 'iesire'}, 
	{'day': 8, 'amount': 52.3, 'type': 'iesire'}, 
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}])
	delete_transaction_type(account, 'iesire')
	assert(account['transactions'] == [])

def test_delete_transaction_day():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 2, 'amount': 6.5, 'type': 'intrare'}, {'day': 1, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	delete_transaction_day(account, 1)
	assert(account['transactions'] == [{'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 2, 'amount': 6.5, 'type': 'intrare'}])
	delete_transaction_day(account, 2)
	assert(account['transactions'] == [])

def test_delete_transaction_range():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	delete_transaction_range(account, 1, 2)
	assert(account['transactions'] == [{'day': 21, 'amount': 6.5, 'type': 'intrare'}, 
	{'day': 8, 'amount': 52.3, 'type': 'iesire'}])
	delete_transaction_range(account, 5, 20)
	assert(account['transactions'] == [{'day': 21, 'amount': 6.5, 'type': 'intrare'}])
	delete_transaction_range(account, 20, 30)
	assert(account['transactions'] == [])

def test_search_transaction_bigger():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	assert(search_transaction_bigger(account, 42, _pass))
	assert(not search_transaction_bigger(account, 52.3, _pass))
	assert(search_transaction_bigger(account, 52.2, _pass))
	assert(search_transaction_bigger(account, 1, _pass))

def test_search_transaction_bigger_before_day():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	assert(search_transaction_bigger_before_day(account, 2, 42, _pass))
	assert(not search_transaction_bigger_before_day(account, 10, 52.3, _pass))
	assert(not search_transaction_bigger_before_day(account, 8, 52.2, _pass))
	assert(search_transaction_bigger_before_day(account, 2, 0.4, _pass))

def test_search_transaction_type():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}], 'history': []}
	assert(search_transaction_type(account, 'intrare', _pass))
	assert(not search_transaction_type(account, 'iesire', _pass))

def test_report_type_amount():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	assert(report_type_amount(account, 'intrare') == 49.92)
	assert(report_type_amount(account, 'iesire') == 96.51)

def test_report_balance_date():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	assert(report_balance_date(account, 1) == 1.21)
	assert(report_balance_date(account, 2) == -0.79)
	assert(report_balance_date(account, 10) == -53.09)
	assert(report_balance_date(account, 20) == -53.09)
	assert(report_balance_date(account, 21) == -46.59)

def test_report_order_type_by_amount():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	assert(report_order_type_by_amount(account) == [0, 2, 3, 5, 1, 4])

def test_filter_del_type():
	global TEST_ARRAY
	del TEST_ARRAY[:]
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	filter_del_type(account, 'intrare', add_to_test_array)
	assert(TEST_ARRAY == [{'day': 2, 'amount': 2.0, 'type': 'iesire'}, 
	{'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}])
	del TEST_ARRAY[:]
	filter_del_type(account, 'iesire', add_to_test_array)
	assert(TEST_ARRAY == [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}])

def test_filter_del_type_rm():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	filter_del_type_rm(account, 'intrare')
	assert(account['transactions'] == [{'day': 2, 'amount': 2.0, 'type': 'iesire'}, 
	{'day': 8, 'amount': 52.3, 'type': 'iesire'}, 
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}])
	filter_del_type_rm(account, 'iesire')
	assert(account['transactions'] == [])

def test_filter_smaller_by_type():
	global TEST_ARRAY
	del TEST_ARRAY[:]
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	filter_smaller_by_type(account, 42.42, 'intrare', add_to_test_array)
	assert(TEST_ARRAY == [{'day': 8, 'amount': 52.3, 'type': 'iesire'}])
	del TEST_ARRAY[:]
	filter_smaller_by_type(account, 42.22, 'iesire', add_to_test_array)
	assert(TEST_ARRAY == [{'day': 1, 'amount': 42.42, 'type': 'intrare'}])

def test_filter_smaller_by_type_rm():
	account = {'transactions': [{'day': 1, 'amount': 1.0, 'type': 'intrare'}, 
	{'day': 1, 'amount': 42.42, 'type': 'intrare'}, {'day': 2, 'amount': 2.0, 'type': 'iesire'},
	{'day': 21, 'amount': 6.5, 'type': 'intrare'}, {'day': 8, 'amount': 52.3, 'type': 'iesire'},
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}], 'history': []}
	filter_smaller_by_type_rm(account, 42, 'intrare')
	assert(account['transactions'] == [{'day': 1, 'amount': 42.42, 'type': 'intrare'}, 
	{'day': 2, 'amount': 2.0, 'type': 'iesire'}, 
	{'day': 8, 'amount': 52.3, 'type': 'iesire'}, 
	{'day': 1, 'amount': 42.21, 'type': 'iesire'}])
	filter_smaller_by_type_rm(account, 52.3, 'iesire')
	assert(account['transactions'] == [{'day': 1, 'amount': 42.42, 'type': 'intrare'},
	{'day': 8, 'amount': 52.3, 'type': 'iesire'}])
	
def test_undo():
	account = {'transactions': [{'testing': 1}, {'is': 0}, {'divine': 10}],
	'history': [[], [{'testing': 1}, {'is': 0}], 
	[{'not': 0}, {'testing': 1}, {'is': 0}, {'divine': 10}]]}
	undo(account)
	assert(account == {'transactions': [{'not': 0}, {'testing': 1}, {'is': 0}, {'divine': 10}],
	'history': [[], [{'testing': 1}, {'is': 0}]]})
	undo(account)
	assert(account == {'transactions': [{'testing': 1}, {'is': 0}],
	'history': [[]]})
	undo(account)
	assert(account == {'transactions': [], 'history': []})