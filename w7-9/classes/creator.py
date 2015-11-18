from classes.repository import BookRepository, ClientRepository
from classes.controller import Controller, BookController, ClientController
from classes.ui import UI

class Creator(object):
	"""docstring for Creator"""
	def getClientRepository(self):
		return ClientRepository()

	def getBookRepository(self):
		return BookRepository()

	def getBookController(self):
		return BookController(self.getBookRepository())

	def getClientController(self):
		return ClientController(self.getClientRepository())

	def getController(self):
		return Controller()

	def getUI(self):
		return UI(self.getController(), self.getClientController(), self.getBookController())
