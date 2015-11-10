from classes.repository import Repository
from classes.controller import Controller
from classes.ui import UI

class Creator(object):
	"""docstring for Creator"""
	def getRepository(self):
		return Repository()

	def getController(self):
		return Controller(self.getRepository())

	def getUI(self):
		return UI(Controller(self.getRepository()))
