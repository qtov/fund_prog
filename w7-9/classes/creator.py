from classes.repository import BookRepository, ClientRepository
from classes.controller import Controller, BookController, ClientController
from classes.ui import UI

class Creator(object):
	"""docstring for Creator"""
	def getRepository(self, type_):
		if (type_ == 'client'):
			return ClientRepository()
		elif (type_ == 'book'):
			return BookRepository()
		else:
			raise NameError

	def getBookController(self):
		return BookController(self.getRepository('book'))

	def getClientController(self):
		return ClientController(self.getRepository('client'))

	def getController(self):
		return Controller(self.getBookController(), self.getClientController())

	def getUI(self):
		return UI(self.getController())
