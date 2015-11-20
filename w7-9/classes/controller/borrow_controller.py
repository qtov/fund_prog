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
			return ('Carte returnata.')
		else:
			self.__repository.add(borrow)
			return ('Carte imprumutata.')
