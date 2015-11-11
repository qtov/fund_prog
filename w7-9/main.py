from classes.creator import Creator
from classes.ui import UI
from classes.validator import Validator

def test_all():
	Validator.testValidateOption()
	Validator.testValidateTitle()
	Validator.testValidateCNP()
	Validator.testValidateName()

def main():
	creator = Creator()
	ui = creator.getUI()
	ui.read_option()

if (__name__ == '__main__'):
	test_all()
	main()
