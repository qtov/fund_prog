from classes.domain.book import Book
from classes.response import Response

class BookController(object):
	def __init__(self, repository, validator, utils):
		self.__repository = repository
		self.__validator = validator
		self.__utils = utils

	def add(self, title, description, author):
		"""Trimite un obiect Book la repository pentru a-l adauga."""
		response = Response()
		try:
			self.__validator.validateTitle(title)
		except ValueError as err:
			response.add('error', err.args[0])
		try:
			self.__validator.validateName(author)
		except ValueError as err:
			response.add('error', 'Numele autorului este invalid.')
		if (response.is_successful()):
			book = Book(self.__utils.getMaxUid('book') + 1, title, description, author)
			added = self.__repository.add(book)
			if (not added):
				response.add('error', 'Cartea exista.')
			#return self.__repository.add(book)
		return response

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

	def edit(self, pos, title, description, author):
		response = Response()
		try:
			self.__validator.validateTitle(title)
		except ValueError as err:
			response.add('error', err.args[0])
		try:
			self.__validator.validateName(author)
		except ValueError as err:
			response.add('error', err.args[0])
		if (response.is_successful()):
			self.__repository.edit(pos, title, description, author)
			response.add('success', 'Cartea a fost actualizata.')
		return response

	def display(self):
		"""Afiseaza lista de obiecte de tip Book din repository."""
		return (self.__repository.show())

	def search(self, argument, type_):
		if (self.__repository.search(argument, type_) == []):
			return ('Nu s-a gasit nici o carte.' + "\n" + '-------=======-------' + "\n")
		else:
			return self.__repository.search(argument, type_)

	def get_obj_from_id(self, uid):
		return self.__repository.get_obj_from_id(uid)

	def get_objs_from_title(self, title):
		return self.__repository.get_objs_from_title(title)

	def get_objs_from_author(self, author):
		return self.__repository.get_objs_from_author(author)

