import re
from classes.book import Book
from classes.client import Client

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
		repository = open("repositories/book_repository", "a")
		repository.write(str(book))
		repository.close()
		self.__list.append(book)

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
				if (item.getTitle() == title):
					self.__list.remove(item)
					deleted = True
		self.updateFile()

	def delete_author(self, author):
		"""Sterge un element dupa autor."""
		deleted = True
		while (deleted):
			deleted = False
			for item in self.__list:
				if (item.getAuthor() == author):
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

	def edit(self, pos, title, description, author):
		"""Editeaza cartea de pe pozitia pos"""
		self.__list[pos].setTitle(title)
		self.__list[pos].setDescription(description)
		self.__list[pos].setAuthor(author)

class ClientRepository(object):
	"""Client repository."""
	def __init__(self):
		self.__list = self.getList()

	def getList(self):
		"""
		Ia datele din fisier si construieste obiecte pe care
		le pune intr-o lista pe care o returneaza.
		"""
		__list = []
		per = 0
		attr = [0] * 3
		repository = open("repositories/client_repository", "r")
		for line in repository.readlines():
			# print(line, per)
			try:
				if (per == 0):
					item = re.match("^\w+:\s(\d+)$", line)
					attr[per] = item.group(1)
				elif (per <= 2):
					item = re.match("^\w+:\s\"(.+)\"$", line)
					attr[per] = item.group(1)
				if (per == 3):
					client = Client(attr[0], attr[1], attr[2])
					per = -1
					__list.append(client)
			except AttributeError:
				pass
			per += 1
		repository.close()
		return __list

	def show(self):
		"""Afiseaza lista de obiecte."""
		new_list = []
		for item in self.__list:
			new_list.append(item)
		return (new_list)

	def updateFile(self):
		"""Actualizeaza fisierul."""
		repository = open("repositories/client_repository", "w")
		for item in self.__list:
			repository.write(str(item))
		repository.close()

	def add(self, client):
		"""Adauga un client"""
		repository = open("repositories/client_repository", "a")
		repository.write(str(client))
		repository.close()
		self.__list.append(client)

	def delete_id(self, uid):
		"""Sterge un client in functie de id."""
		deleted = True
		while (deleted):
			deleted = False
			for item in self.__list:
				if (item.getUid() == uid):
					self.__list.remove(item)
					deleted = True
		self.updateFile()

	def delete_name(self, name):
		"""Sterge un client in functie de nume."""
		deleted = True
		while (deleted):
			deleted = False
			for item in self.__list:
				if (item.getName() == name):
					self.__list.remove(item)
					deleted = True
		self.updateFile()

	def delete_cnp(self, cnp):
		"""Sterge un client in functie de cnp."""
		deleted = True
		while (deleted):
			deleted = False
			for item in self.__list:
				if (item.getCNP() == cnp):
					self.__list.remove(item)
					deleted = True
		self.updateFile()
