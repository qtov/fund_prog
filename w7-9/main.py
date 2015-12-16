from classes.creator import Creator
from classes.validator import Validator
from unittest import FunctionTestCase

def test_all():
	validator = Validator()
	# validator.testValidateOption()
	# validator.testValidateTitle()
	# validator.testValidateCNP()
	# validator.testValidateName()
	testcase = FunctionTestCase(validator.testValidateOption())
	testcase = FunctionTestCase(validator.testValidateTitle())
	testcase = FunctionTestCase(validator.testValidateCNP())
	testcase = FunctionTestCase(validator.testValidateName())

def main():
	creator = Creator()
	ui = creator.getMenu()
	ui.read_option()

if (__name__ == '__main__'):
	test_all()
	main()
