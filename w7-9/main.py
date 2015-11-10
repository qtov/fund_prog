from classes.creator import Creator
from classes.ui import UI

def test_all():
	pass

def main():
	creator = Creator()
	ui = creator.getUI()
	ui.read_option()

if (__name__ == '__main__'):
	test_all()
	main()
