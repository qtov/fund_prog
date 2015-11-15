import re
from classes.book import Book
from classes.client import Client

class BookRepository(object):
	"""Repository"""
	def __init__(self):
		self.__list = self.getList()
		
	def getList(self):
		__list = []
		per = 0
		attr = [0] * 4
		repository = open("repositories/book_repository", "r")
		for line in repository.readlines():
			print(line, per)
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
		repository = open("repositories/book_repository", "a")
		repository.write(str(book))
		repository.close()
		self.__list.append(book)

	def show(self):
		for item in self.__list:
			print(item, end="")

	def updateFile(self):
		repository = open("repositories/book_repository", "w")
		for item in self.__list:
			repository.write(str(item))
		repository.close()

	def delete_id(self, uid):
		deleted = True
		while (deleted):
			deleted = False
			for item in self.__list:
				if (item.getUid() == uid):
					self.__list.remove(item)
					deleted = True
		self.updateFile()

	def delete_title(self, title):
		deleted = True
		while (deleted):
			deleted = False
			for item in self.__list:
				if (item.getTitle() == title):
					self.__list.remove(item)
					deleted = True
		self.updateFile()

	def delete_author(self, author):
		deleted = True
		while (deleted):
			deleted = False
			for item in self.__list:
				if (item.getAuthor() == author):
					self.__list.remove(item)
					deleted = True
		self.updateFile()

class ClientRepository(object):
	"""Client repository."""
	def __init__(self):
		self.__list = self.getList()

	def getList(self):
		__list = []
		per = 0
		attr = [0] * 3
		repository = open("repositories/client_repository", "r")
		for line in repository.readlines():
			print(line, per)
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
		for item in self.__list:
			print(item, end="")

	def updateFile(self):
		repository = open("repositories/client_repository", "w")
		for item in self.__list:
			repository.write(str(item))
		repository.close()

	def add(self, client):
		repository = open("repositories/client_repository", "a")
		repository.write(str(client))
		repository.close()
		self.__list.append(client)
