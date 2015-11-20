import re

class Validator(object):
	def validateOption(self, opt, min_, max_):
		"""Valideaza optiunea sa fie un intreg care apartine [min_, max_]"""
		try:
			opt = int(opt)
		except ValueError:		
			raise ValueError('Optiune invalida, introduceti un intreg.')
		if (opt < min_ or opt > max_):
			raise ValueError('Optiunea nu se incadreaza in interval.')
	
	def testValidateOption(self):
		self.validateOption(1, 1, 3)
		self.validateOption(2, 1, 3)
		self.validateOption(3, 1, 3)
		try:
			self.validateOption(6, 1, 3)
			assert(0 == 1)
		except ValueError:
			pass
		self.validateOption(5, 1, 10)
		self.validateOption(7, 6, 11)
		self.validateOption(3, 3, 4)
	
	def validateTitle(self, title):
		"""Valideaza titlul. Acesta sa existe."""
		if (len(title) == 0):
			raise ValueError('Titlu inexistent...')
	
	def testValidateTitle(self):
		self.validateTitle('as')
		try:
			self.validateTitle('')
			assert(0 == 1)
		except ValueError:
			pass
		self.validateTitle('re')
		self.validateTitle('as')
	
	def validateCNP(self, cnp):
		"""Valideaza CNP"""
		reMatch = re.match("^([12][0-9]{2}(?:(?:0[1-9])|(?:1[0-2]))(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))[0-9]{6})$", cnp, re.IGNORECASE)
		if (not reMatch):
			raise ValueError('CNP invalid...')
	
	def testValidateCNP(self):
		self.validateCNP('1951113451651')
		self.validateCNP('1951104451651')
		self.validateCNP('1951231451651')
		try:
			self.validateCNP('3951113451651')
			assert(0 == 1)
		except ValueError:
			pass
		try:
			self.validateCNP('1951313451651')
			assert(0 == 1)
		except ValueError:
			pass
		try:
			self.validateCNP('1951135451651')
			assert(0 == 1)
		except ValueError:
			pass
	
	def validateName(self, name):
		"""Valideaza nume. De forma "Popescu Ion", "Popescu Ion Marian", "Pepescu Ion-Marian", "Popescu-Ion Marian" """
		reMatch = re.match("^([a-z]{3,15}(?:-[a-z]{3,15})?\s[a-z]{3,15}(?:-[a-z]{3,15})?(?:\s[a-z]{3,15}(?:-[a-z]{3,15})?)?)$", name, re.IGNORECASE)
		if (not reMatch):
			raise ValueError('Nume invalid...')
	
	def testValidateName(self):
		self.validateName('Something Good')
		self.validateName('Something Very-Good')
		self.validateName('Cookies Mister Potato')
		try:
			self.validateName('Bob')
			assert(0 == 1)
		except ValueError:
			pass
		try:
			self.validateName('Bob Marley The Mighty Cucumber')
			assert(0 == 1)
		except ValueError:
			pass
		try:
			self.validateName('01000010 01011010')
			assert(0 == 1)
		except ValueError:
			pass
