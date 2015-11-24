from classes.domain.borrow import Borrow

class BorrowController(object):
	def __init__(self, repository, validator):
		self.__repository = repository
		self.__validator = validator

	def add_remove(self, uid_c, uid_b):
		self.__validator.isNumber(uid_c)
		self.__validator.isNumber(uid_b)
		borrow = Borrow(uid_c, uid_b)
		if (self.__repository.exists(borrow)):
			self.__repository.remove(borrow)
			return False
		else:
			self.__repository.add(borrow)
			return True

	def check_if_exists_client(self, uid):
		return self.__repository.check_if_exists_client(uid)

	def check_if_exists_book(self, uid):
		return self.__repository.check_if_exists_book(uid)

	def getReverseListBooks(self):
		return self.__repository.getReverseListBooks()

	def getReverseListClients(self):
		return self.__repository.getReverseListClients()

	def getClientIds(self):
		return self.__repository.getClientIds()

	def getBooksByClient(self, uid):
		return self.__repository.getBooksByClient(uid)
