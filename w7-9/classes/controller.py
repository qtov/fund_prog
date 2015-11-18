from classes.validator import Validator, re
from classes.book import Book
from classes.client import Client
from classes.utils import Utils

class Controller(object):
	"""docstring for Controller"""
	def __init__(self):
		pass

	def take_option(self, option):
		Validator.validateOption(option, 1, 8)

	def take_suboption(self, suboption):
		Validator.validateOption(suboption, 1, 3)

	def take_x_option_book(self, x_option):
		Validator.validateOption(x_option, 1, 3)

class BookController(object):
	"""docstring for Controller"""
	def __init__(self, repository):
		self.__repository = repository

	def add(self, title, description, author):
		Validator.validateTitle(title)
		Validator.validateName(author)
		book = Book(Utils.getMaxUid('book') + 1, title, description, author)
		self.__repository.add(book)

	def delete_id(self, uid):
		self.__repository.delete_id(uid)

	def delete_title(self, title):
		self.__repository.delete_title(title)

	def delete_author(self, author):
		self.__repository.delete_author(author)

	def display(self):
		return (self.__repository.show())

class ClientController(object):
	"""docstring for Controller"""
	def __init__(self, repository):
		self.__repository = repository

	def validateData(self, name, cnp):
		Validator.validateName(name)
		Validator.validateCNP(cnp)

	def add(self, name, cnp):
		self.validateData(name, cnp)
		client = Client(Utils.getMaxUid('client') + 1, name, cnp)
		self.__repository.add(client)

	def display(self):
		return (self.__repository.show())

	def delete_id(self, uid):
		self.__repository.delete_id(uid)

	def delete_name(self, name):
		self.__repository.delete_name(name)

	def delete_cnp(self, cnp):
		self.__repository.delete_cnp(cnp)
