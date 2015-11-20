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
			repository.write(item)
		repository.close()

	def exists(self, borrow):
		for item in self.__list:
			if (item == borrow):
				return True
		return False
