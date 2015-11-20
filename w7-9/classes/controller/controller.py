class Controller(object):
	def __init__(self, validator):
		self.__validator = validator

	def take_option(self, option):
		"""Primeste optiunea si o valideaza."""
		self.__validator.validateOption(option, 1, 8)

	def take_suboption(self, suboption):
		"""Primeste optiunea si o valideaza."""
		self.__validator.validateOption(suboption, 1, 3)

	def take_x_suboption(self, x_option):
		"""Primeste optiunea si o valideaza."""
		self.__validator.validateOption(x_option, 1, 4)
