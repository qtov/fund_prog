from classes.validator import Validator, re
from classes.book import Book
from classes.client import Client
from functions.utils import getMaxUid

class Controller(object):
	"""docstring for Controller"""
	def __init__(self, book_controller, client_controller):
		self.book = book_controller
		self.client = client_controller
	
	def __set_option(self, option):
		self.book.setOption(option)
		self.client.setOption(option)

	def __set_suboption(self, suboption):
		self.book.setSuboption(suboption)
		self.client.setSuboption(suboption)

	def take_option(self, option):
		Validator.validateOption(option, 1, 8)
		self.__set_option(int(option))

	def take_suboption(self, suboption):
		Validator.validateOption(suboption, 1, 3)
		self.__set_suboption(int(suboption))

	def take_x_option_book(self, x_option):
		Validator.validateOption(x_option, 1, 3)
		self.__set_x_option(int(x_option))

class BookController(object):
	"""docstring for Controller"""
	def __init__(self, repository):
		self.__repository = repository

	def setOption(self, option):
		self.__option = option

	def setSuboption(self, suboption):
		self.__suboption = suboption
		
	def add(self, title, description, author):
		Validator.validateTitle(title)
		book = Book(getMaxUid('book') + 1, title, description, author)
		self.__repository.add(book)

	def delete_id(self, uid):
		self.__repository.delete_id(uid)

	def delete_title(self, title):
		self.__repository.delete_title(title)

	def delete_author(self, author):
		self.__repository.delete_author(author)

	def display(self):
		self.__repository.show()

class ClientController(object):
	"""docstring for Controller"""
	def __init__(self, repository):
		self.__repository = repository

	def setOption(self, option):
		self.__option = option

	def setSuboption(self, suboption):
		self.__suboption = suboption

	def validateData(self, name, cnp):
		Validator.validateName(name)
		Validator.validateCNP(cnp)

	def add(self, name, cnp):
		self.validateData(name, cnp)
		client = Client(getMaxUid('client') + 1, name, cnp)
		self.__repository.add(client)

	def display(self):
		self.__repository.show()
