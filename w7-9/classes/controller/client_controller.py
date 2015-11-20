from classes.domain.client import Client

class ClientController(object):
	def __init__(self, repository, validator, utils):
		self.__repository = repository
		self.__validator = validator
		self.__utils = utils

	def validateName(self, name):
		self.__validator.validateName(name)

	def validateCNP(self, cnp):
		self.__validator.validateCNP(cnp)

	def check_uid(self, uid):
		"""Trimite id-ul elementului care trebuie modificat la repository."""
		return (self.__repository.check_if_exists(uid))

	def check_cnp(self, cnp):
		"""Trimite cnp-ul elementului care trebuie modificat la repository."""
		return (self.__repository.check_if_exists_cnp(cnp))

	def edit(self, pos, name, cnp):
		self.__validator.validateName(name)
		self.__validator.validateCNP(cnp)
		self.__repository.edit(pos, name, cnp)

	def validateData(self, name, cnp):
		"""Trimite datele la self.__validator.pentru a le valida."""
		self.validateName(name)
		self.validateCNP(cnp)

	def add(self, name, cnp):
		"""Trimite un obiect Client la repository pentru a-l adauga."""
		self.validateData(name, cnp)
		client = Client(self.__utils.getMaxUid('client') + 1, name, cnp)
		return self.__repository.add(client)

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

	def search(self, argument, type_):
		if (self.__repository.search(argument, type_) == []):
			return ('Nu s-a gasit nici un client.' + "\n" + '-------=======-------' + "\n")
		else:
			return self.__repository.search(argument, type_)
