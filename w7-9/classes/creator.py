from classes.ui.menu import Menu
from classes.repository.book_repository import BookRepository
from classes.repository.client_repository import ClientRepository
from classes.repository.borrow_repository import BorrowRepository
from classes.controller.controller import Controller
from classes.controller.client_controller import ClientController
from classes.controller.book_controller import BookController
from classes.controller.borrow_controller import BorrowController
from classes.validator import Validator
from classes.utils import Utils

class Creator(object):
	"""docstring for Creator"""
	def getClientRepository(self):
		return ClientRepository()

	def getBookRepository(self):
		return BookRepository()

	def getBookController(self):
		return BookController(self.getBookRepository(), self.getValidator(), self.getUtils())

	def getClientController(self):
		return ClientController(self.getClientRepository(), self.getValidator(), self.getUtils())

	def getController(self):
		return Controller(self.getValidator())

	def getBorrowRepository(self):
		return BorrowRepository()

	def getBorrowController(self):
		return BorrowController(self.getBorrowRepository(), self.getValidator())

	def getMenu(self):
		return Menu(self.getController(), self.getClientController(), self.getBookController(), self.getBorrowController())

	def getValidator(self):
		return Validator()

	def getUtils(self):
		return Utils()
