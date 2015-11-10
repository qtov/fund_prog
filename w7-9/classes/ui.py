class UI(object):
	"""docstring for UI"""

	def __init__(self, controller):
		self.__exit_option = '8';
		self.__exit_suboption = '3';
		self.__controller = controller

	def show_menu(self):
		print(end="\n")
		print('1. Adaugare.')
		print('2. Sterge.')
		print('3. Modificare.')
		print('4. Cautare.')
		print('5. Inchiriere/returnare.')
		print('6. Rapoarte.')
		print('7. Afisare.')
		print('8. Iesire.')

	def show_ext_menu(self):
		print('1. Carte.')
		print('2. Client.')
		print('3. Inapoi.')

	def _read_book(self):
		title = input('Introduceti titlul: ')
		description = input('Introduceti descrierea: ')
		try:
			self.__controller.take_book(title, description)
		except ValueError as err:
			print(err.args[0])

	def _read_client(self):
		name = input('Introduceti numele: ')
		cnp = input('Introduceti CNP-ul: ')
		try:
			self.__controller.take_client(name, cnp)
		except ValueError as err:
			print(err.args[0])

	def _read_categ(self):
		suboption = None
		while (suboption != self.__exit_suboption):
			self.show_ext_menu()
			suboption = input('Introduceti categoria: ')
			try:
				if (suboption != self.__exit_suboption):
					self.__controller.take_suboption(suboption)
					if (suboption == '1'):
						self._read_book()
					elif (suboption == '2'):
						self._read_client()
					suboption = self.__exit_suboption
			except ValueError as err:
				print(err.args[0])

	def read_option(self):
		option = None
		while (option != self.__exit_option):
			self.show_menu()
			option = input('Introduceti optiunea: ')
			try:
				self.__controller.take_option(option)			
				if (int(option) <= 4):
					self._read_categ()
			except ValueError as err:
				print(err.args[0])
