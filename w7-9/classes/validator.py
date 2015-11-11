import re

class Validator(object):
	"""docstring for Validator"""

	@staticmethod
	def validateOption(opt, min_, max_):
		try:
			opt = int(opt)
		except ValueError:		
			raise ValueError('Optiune invalida, introduceti un intreg.')
		if (opt < min_ or opt > max_):
			raise ValueError('Optiunea nu se incadreaza in interval.')

	@staticmethod
	def testValidateOption():
		Validator.validateOption(1, 1, 3)
		Validator.validateOption(2, 1, 3)
		Validator.validateOption(3, 1, 3)
		try:
			Validator.validateOption(6, 1, 3)
			assert(0 == 1)
		except ValueError:
			pass
		Validator.validateOption(5, 1, 10)
		Validator.validateOption(7, 6, 11)
		Validator.validateOption(3, 3, 4)


	@staticmethod
	def validateTitle(title):
		if (len(title) == 0):
			raise ValueError('Titlu inexistent...')

	@staticmethod
	def testValidateTitle():
		Validator.validateTitle('as')
		try:
			Validator.validateTitle('')
			assert(0 == 1)
		except ValueError:
			pass
		Validator.validateTitle('re')
		Validator.validateTitle('as')


	@staticmethod
	def validateCNP(cnp):
		# if (len(cnp) != 13):
		# 	raise ValueError('CNP invalid...')
		reMatch = re.match("^([12][0-9]{2}(?:(?:0[1-9])|(?:1[0-2]))(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))[0-9]{6})$", cnp, re.IGNORECASE)
		if (not reMatch):
			raise ValueError('CNP invalid...')

	@staticmethod
	def testValidateCNP():
		Validator.validateCNP('1951113451651')
		Validator.validateCNP('1951104451651')
		Validator.validateCNP('1951231451651')
		try:
			Validator.validateCNP('3951113451651')
			assert(0 == 1)
		except ValueError:
			pass
		try:
			Validator.validateCNP('1951313451651')
			assert(0 == 1)
		except ValueError:
			pass
		try:
			Validator.validateCNP('1951135451651')
			assert(0 == 1)
		except ValueError:
			pass


	@staticmethod
	def validateName(name):
		reMatch = re.match("^([a-z]{3,15}(?:-[a-z]{3,15})?\s[a-z]{3,15}(?:-[a-z]{3,15})?(?:\s[a-z]{3,15}(?:-[a-z]{3,15})?)?)$", name, re.IGNORECASE)
		if (not reMatch):
			raise ValueError('Nume invalid...')

	@staticmethod
	def testValidateName():
		Validator.validateName('Something Good')
		Validator.validateName('Something Very-Good')
		Validator.validateName('Cookies Mister Potato')
		try:
			Validator.validateName('Bob')
			assert(0 == 1)
		except ValueError:
			pass
		try:
			Validator.validateName('Bob Marley The Mighty Cucumber')
			assert(0 == 1)
		except ValueError:
			pass
		try:
			Validator.validateName('01000010 01011010')
			assert(0 == 1)
		except ValueError:
			pass
