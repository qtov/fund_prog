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
	def validateTitle(title):
		if (len(title) == 0):
			raise ValueError('Titlu inexistent...')

	@staticmethod
	def validateCNP(cnp):
		# if (len(cnp) != 13):
		# 	raise ValueError('CNP invalid...')
		reMatch = re.match("([12][0-9]{2}(?:(?:0[1-9])|(?:1[0-2]))(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))[0-9]{6})", cnp, re.IGNORECASE)
		if (not reMatch):
			raise ValueError('CNP invalid...')
			

	@staticmethod
	def validateName(name):
		reMatch = re.match("([a-z]{3,15}(?:-[a-z]{3,15})?\s[a-z]{3,15}(?:-[a-z]{3,15})?(?:\s[a-z]{3,15}(?:-[a-z]{3,15})?)?)", name, re.IGNORECASE)
		if (not reMatch):
			raise ValueError('Nume invalid...')
