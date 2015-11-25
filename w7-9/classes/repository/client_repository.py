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
		attr = [0] * 4
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
				elif (per == 3):
					item = re.match("^\w+:\s(\d+)$", line)
					attr[per] = item.group(1)
				if (per == 4):
					client = Client(attr[0], attr[1], attr[2], int(attr[3]))
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
		self.__list = self.getList()
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

	def get_objs_from_name(self, name):
		new_list = []
		for item in self.__list:
			if (item.getName().lower() == name.lower()):
				new_list.append(item)
		return new_list

	def get_obj_from_cnp(self, cnp):
		for item in self.__list:
			if (item.getCNP() == cnp):
				return item
		return None

	def getListFromIdsOrderName(self, list_):
		"""Returneaza lista ordonata dupa nume."""
		new_list = []
		for item in list_:
			new_list.append(self.get_obj_from_id(item))
		ordered = False
		while (not ordered):
			ordered = True
			i = 0
			while (i < len(new_list) - 1):
				if (new_list[i].getName() > new_list[i + 1].getName()):
					aux = new_list[i]
					new_list[i] = new_list[i + 1]
					new_list[i + 1] = aux
					ordered = False
				i += 1
		return new_list

	def getListFromIdsOrderBooks(self, list_):
		"""Modifica lista cu id-urile corespunzatoare intr-o lista de clienti dupa care o returneaza"""
		new_list = []
		for item in list_:
			new_list.append(self.get_obj_from_id(item['id']))
		return new_list

	def inc_borrow(self, uid):
		"""Incrementeaza punctele utilizatorului."""
		for item in self.__list:
			if (item.getUid() == uid):
				item.incBorrow()
		self.updateFile()

	def getMost20ActiveClients(self):
		"""Returneaza lista celor mai activi 20% clienti."""
		new_list = []
		for item in self.__list:
			new_list.append(item)
		percent_20 = len(new_list) * 0.2
		ordered = False
		while (not ordered):
			ordered = True
			i = 0
			while (i < len(new_list) - 1):
				if (new_list[i].getPoints() < new_list[i + 1].getPoints()):
					aux = new_list[i]
					new_list[i] = new_list[i + 1]
					new_list[i + 1] = aux
					ordered = False
				i += 1
		new_list_percent_20 = []
		for item in new_list:
			if (percent_20 > 0):
				new_list_percent_20.append(item)
				percent_20 -= 1
			else:
				break
		return new_list_percent_20
