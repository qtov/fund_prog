from classes.domain.book import Book

class BookController(object):
	def __init__(self, repository, validator, utils):
		self.__repository = repository
		self.__validator = validator
		self.__utils = utils

	def add(self, title, description, author):
		"""Trimite un obiect Book la repository pentru a-l adauga."""
		self.__validator.validateTitle(title)
		self.__validator.validateName(author)
		book = Book(self.__utils.getMaxUid('book') + 1, title, description, author)
		return self.__repository.add(book)

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
		self.__validator.validateTitle(title)
		self.__validator.validateName(author)
		self.__repository.edit(pos, title, description, author)

	def display(self):
		"""Afiseaza lista de obiecte de tip Book din repository."""
		return (self.__repository.show())

	def search(self, argument, type_):
		if (self.__repository.search(argument, type_) == []):
			return ('Nu s-a gasit nici o carte.' + "\n" + '-------=======-------' + "\n")
		else:
			return self.__repository.search(argument, type_)
