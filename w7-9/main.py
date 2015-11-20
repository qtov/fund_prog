from classes.creator import Creator
from classes.validator import Validator

def test_all():
	validator = Validator()
	validator.testValidateOption()
	validator.testValidateTitle()
	validator.testValidateCNP()
	validator.testValidateName()

def main():
	creator = Creator()
	ui = creator.getMenu()
	ui.read_option()

if (__name__ == '__main__'):
	test_all()
	main()
