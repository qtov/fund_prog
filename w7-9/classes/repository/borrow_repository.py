import re
from classes.domain.borrow import Borrow

class BorrowRepository(object):
	def __init__(self):
		self.__list = self.getList()

	def add(self, borrow):
		repository = open("repositories/borrow_repository", "a")
		repository.write(str(borrow))
		repository.close()
		self.__list.append(borrow)
		return True

	def remove(self, borrow):
		for item in self.__list:
			if (borrow == item):
				self.__list.remove(item)
		self.updateFile()

	def getList(self):
		"""
		Ia datele din fisier si construieste obiecte pe care
		le pune intr-o lista pe care o returneaza.
		"""
		__list = []
		repository = open("repositories/borrow_repository", "r")
		for line in repository.readlines():
			try:
				reMatch = re.match("^\w+\s(\d+)\s->\s\w+\s(\d+)$", line, re.I)
				borrow = Borrow(reMatch.group(1), reMatch.group(2))
				__list.append(borrow)
			except AttributeError:
				pass
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
		repository = open("repositories/borrow_repository", "w")
		for item in self.__list:
			repository.write(str(item))
		repository.close()

	def exists(self, borrow):
		for item in self.__list:
			if (item == borrow):
				return True
		return False

	def check_if_exists_client(self, uid):
		for item in self.__list:
			if (item.getClient() == uid):
				return True
		return False

	def check_if_exists_book(self, uid):
		for item in self.__list:
			if (item.getBook() == uid):
				return True
		return False

	def getReverseListBooks(self):
		new_list = []
		for item in self.__list:
			added = False
			for book in new_list:
				if (item.getBook() == book['id']):
					book['count'] += 1
					added = True
			if (not added):
				new_list.append({'count': 1, 'id': item.getBook()})
		ordered = False
		while (not ordered):
			ordered = True
			i = 0
			while (i < len(new_list) - 1):
				if (new_list[i]['count'] < new_list[i + 1]['count']):
					aux = new_list[i]
					new_list[i] = new_list[i + 1]
					new_list[i + 1] = aux
					ordered = False
				i += 1
		return new_list

	def getClientIds(self):
		new_list = []
		for item in self.__list:
			found = False
			for client in new_list:
				if (client == item.getClient()):
					found = True
			if (not found):
				new_list.append(item.getClient())
		return new_list

	def getReverseListClients(self):
		new_list = []
		for item in self.__list:
			added = False
			for client in new_list:
				if (item.getClient() == client['id']):
					client['count'] += 1
					added = True
			if (not added):
				new_list.append({'count': 1, 'id': item.getClient()})
		ordered = False
		while (not ordered):
			ordered = True
			i = 0
			while (i < len(new_list) - 1):
				if (new_list[i]['count'] < new_list[i + 1]['count']):
					aux = new_list[i]
					new_list[i] = new_list[i + 1]
					new_list[i + 1] = aux
					ordered = False
				i += 1
		return new_list
