from classes.validator import Validator, re
from classes.book import Book
from classes.client import Client
from classes.utils import Utils

class Controller(object):
	def __init__(self):
		pass

	def take_option(self, option):
		"""Primeste optiunea si o valideaza."""
		Validator.validateOption(option, 1, 8)

	def take_suboption(self, suboption):
		"""Primeste optiunea si o valideaza."""
		Validator.validateOption(suboption, 1, 3)

	def take_x_option_book(self, x_option):
		"""Primeste optiunea si o valideaza."""
		Validator.validateOption(x_option, 1, 3)

class BookController(object):
	def __init__(self, repository):
		self.__repository = repository

	def add(self, title, description, author):
		"""Trimite un obiect Book la repository pentru a-l adauga."""
		Validator.validateTitle(title)
		Validator.validateName(author)
		book = Book(Utils.getMaxUid('book') + 1, title, description, author)
		self.__repository.add(book)

	def delete_id(self, uid):
		"""Trimite id-ul elementului care trebuie sters la repository."""
		self.__repository.delete_id(uid)

	def delete_title(self, title):
		"""Trimite titlul elementului care trebuie sters la repository."""
		self.__repository.delete_title(title)

	def delete_author(self, author):
		"""Trimite autorul elementului care trebuie sters la repository."""
		self.__repository.delete_author(author)

	def check_uid(self, uid):
		"""Trimite id-ul elementului care trebuie modificat la repository."""
		return (self.__repository.check_if_exists(uid))

	def edit_uid(self, pos, title, description, author):
		Validator.validateTitle(title)
		Validator.validateName(author)
		self.__repository.edit(pos, title, description, author)

	def display(self):
		"""Afiseaza lista de obiecte de tip Book din repository."""
		return (self.__repository.show())

class ClientController(object):
	def __init__(self, repository):
		self.__repository = repository

	def validateData(self, name, cnp):
		"""Trimite datele la Validator pentru a le valida."""
		Validator.validateName(name)
		Validator.validateCNP(cnp)

	def add(self, name, cnp):
		"""Trimite un obiect Client la repository pentru a-l adauga."""
		self.validateData(name, cnp)
		client = Client(Utils.getMaxUid('client') + 1, name, cnp)
		self.__repository.add(client)

	def display(self):
		"""Afiseaza lista de obiecte de tip Client din repository."""
		return (self.__repository.show())

	def delete_id(self, uid):
		"""Trimite id-ul elementului care trebuie sters la repository."""
		self.__repository.delete_id(uid)

	def delete_name(self, name):
		"""Trimite numele elementului care trebuie sters la repository."""
		self.__repository.delete_name(name)

	def delete_cnp(self, cnp):
		"""Trimite cnp-ul elementului care trebuie sters la repository."""
		self.__repository.delete_cnp(cnp)
