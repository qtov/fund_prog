import re
from classes.domain.book import Book

class BookRepository(object):
	"""Repository"""
	def __init__(self):
		self.__list = self.getList()
		
	def getList(self):
		"""
		Ia datele din fisier si construieste obiecte pe care
		le pune intr-o lista pe care o returneaza.
		"""
		__list = []
		per = 0
		attr = [0] * 4
		repository = open("repositories/book_repository", "r")
		for line in repository.readlines():
			# print(line, per)
			try:
				if (per == 0):
					item = re.match("^\w+:\s(\d+)$", line)
					attr[per] = item.group(1)
				elif (per <= 3):
					item = re.match("^\w+:\s\"(.+)\"$", line)
					attr[per] = item.group(1)
				if (per == 4):
					book = Book(attr[0], attr[1], attr[2], attr[3])
					per = -1
					__list.append(book)
			except AttributeError:
				pass
			per += 1
		repository.close()
		return __list

	def add(self, book):
		"""Adauga un obiect in lista."""
		if (self.check_if_exists_full(book) != -1):
			return False
		repository = open("repositories/book_repository", "a")
		repository.write(str(book))
		repository.close()
		#self.__list.append(book)
		self.__list = self.getList()
		return True

	def show(self):
		"""Afiseaza lista."""
		new_list = []
		for item in self.__list:
			new_list.append(item)
		return (new_list)

	def updateFile(self):
		"""Actualizeaza fisierul in functie de lista."""
		repository = open("repositories/book_repository", "w")
		for item in self.__list:
			repository.write(str(item))
		repository.close()

	def delete_id(self, uid):
		"""Sterge un element dupa id."""
		deleted = True
		while (deleted):
			deleted = False
			for item in self.__list:
				if (item.getUid() == uid):
					self.__list.remove(item)
					deleted = True
		self.updateFile()

	def delete_title(self, title):
		"""Sterge un element dupa titlu."""
		deleted = True
		while (deleted):
			deleted = False
			for item in self.__list:
				if (item.getTitle().lower() == title.lower()):
					self.__list.remove(item)
					deleted = True
		self.updateFile()

	def delete_author(self, author):
		"""Sterge un element dupa autor."""
		deleted = True
		while (deleted):
			deleted = False
			for item in self.__list:
				if (item.getAuthor().lower() == author.lower()):
					self.__list.remove(item)
					deleted = True
		self.updateFile()

	def check_if_exists(self, uid):
		"""Daca exista o carte cu id=uid atunci returneaza pozitia acestuia in lista self.__list"""
		pos = 0
		while (pos < len(self.__list)):
			if (self.__list[pos].getUid() == uid):
				return (pos)
			pos += 1
		return (-1)

	def check_if_exists_full(self, book):
		"""Daca exista o carte la fel atunci returneaza pozitia acestuia in lista self.__list"""
		pos = 0
		while (pos < len(self.__list)):
			if (self.__list[pos] == book):
				return (pos)
			pos += 1
		return (-1)

	def edit(self, pos, title, description, author):
		"""Editeaza cartea de pe pozitia pos"""
		self.__list[pos].setTitle(title)
		self.__list[pos].setDescription(description)
		self.__list[pos].setAuthor(author)
		self.updateFile()

	def search(self, argument, type_):
		"""Cauta un dupa argument si tip."""
		new_list = []
		for item in self.__list:
			if (eval('item.get' + type_ + '()').lower() == argument.lower()):
				new_list.append(item)
		return new_list

	def get_obj_from_id(self, uid):
		for item in self.__list:
			if (item.getUid() == uid):
				return item
		return None

	def get_objs_from_title(self, title):
		new_list = []
		for item in self.__list:
			if (item.getTitle().lower() == title.lower()):
				new_list.append(item)
		return new_list

	def get_objs_from_author(self, author):
		new_list = []
		for item in self.__list:
			if (item.getAuthor().lower() == author.lower()):
				new_list.append(item)
		return new_list
