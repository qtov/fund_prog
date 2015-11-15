from classes.validator import Validator, re

class Controller(object):
	"""docstring for Controller"""
	def __init__(self, repository):
		self.__repository = repository
		
	def take_option(self, option):
		Validator.validateOption(option, 1, 8)
		self.__option = int(option)

	def take_suboption(self, suboption):
		Validator.validateOption(suboption, 1, 2)
		self.__suboption = int(suboption)

	def take_book(self, title, description):
		Validator.validateTitle(title)
		if (self.__option == 1):
			self.__repository.addBook(title, description)
		elif (self.__option == 2):
			pass
		elif (self.__option == 3):
			pass
		elif (self.__option == 4):
			pass
		elif (self.__option == 5):
			pass
		elif (self.__option == 7):
			pass

	def take_client(self, name, cnp):
		Validator.validateName(name)
		Validator.validateCNP(cnp)
		if (self.__option == 1):
			self.__repository.addClient(name, cnp)
		elif (self.__option == 2):
			pass
		elif (self.__option == 3):
			pass
		elif (self.__option == 4):
			pass
		elif (self.__option == 5):
			pass
		elif (self.__option == 7):
			pass
