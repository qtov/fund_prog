def asd():
	raise ValueError

def asd1():
	print('qwe')
	raise ValueError

try:
	asd()
except ValueError:
	asd1()
except ValueError:
	print('potato')
