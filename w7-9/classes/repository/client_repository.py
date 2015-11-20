import re
from classes.domain.client import Client

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

	def check_if_exists_full(self, client):
		"""
		Daca exista un client si returneaza pozitia acestuia in lista self.__list
		In caz contrar returneaza -1
		"""
		pos = 0
		while (pos < len(self.__list)):
			if (self.__list[pos] == client):
				return (pos)
			pos += 1
		return (-1)

	def check_if_exists(self, uid):
		"""
		Daca exista un client si returneaza pozitia acestuia in lista self.__list
		In caz contrar returneaza -1
		"""
		pos = 0
		while (pos < len(self.__list)):
			if (self.__list[pos].getUid() == uid):
				return (pos)
			pos += 1
		return (-1)

	def check_if_exists_cnp(self, cnp):
		"""
		Daca exista un client si returneaza pozitia acestuia in lista self.__list
		In caz contrar returneaza -1
		"""
		pos = 0
		while (pos < len(self.__list)):
			if (self.__list[pos].getCNP() == cnp):
				return (pos)
			pos += 1
		return (-1)

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
		if (self.check_if_exists_full(client) != -1):
			return False
		repository = open("repositories/client_repository", "a")
		repository.write(str(client))
		repository.close()
		self.__list.append(client)
		return True

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
				if (item.getName().lower() == name.lower()):
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

	def edit(self, pos, name, cnp):
		"""Editeaza cartea de pe pozitia pos"""
		self.__list[pos].setName(name)
		self.__list[pos].setCNP(cnp)
		self.updateFile()

	def search(self, argument, type_):
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
