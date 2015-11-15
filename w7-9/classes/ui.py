class UI(object):
	"""docstring for UI"""

	def __init__(self, controller):
		self.__exit_option = 8;
		self.__exit_suboption = 3;
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

	def show_categ_menu(self):
		print('1. Carte.')
		print('2. Client.')
		print('3. Inapoi.')

	def _read_book(self):
		"""Citeste datele unei carti."""
		title = input('Introduceti titlul: ')
		description = input('Introduceti descrierea: ')
		author = input('Introduceti autorul: ')
		try:
			self.__controller.book.add(title, description, author)
		except ValueError as err:
			print(err.args[0])

	def _read_book_id(self):
		uid = input('Id: ')
		return uid

	def _read_book_title(self):
		title = input('Titlu: ')
		return title

	def _read_book_author(self):
		author = input ('Author: ')
		return author

	def _read_client(self):
		"""Citeste datele unui client."""
		name = input('Introduceti numele: ')
		cnp = input('Introduceti CNP-ul: ')
		try:
			self.__controller.client.add(name, cnp)
		except ValueError as err:
			print(err.args[0])

	def show_x_menu_book(self):
		print('1. Id.')
		print('2. Titlu.')
		print('3. Autor.')
		print('4. Inapoi.')

	def _read_x_categ_book(self, for_what):
		self.show_x_menu_book()
		x_type = input('Introduceti tipul pentru ' + for_what + ': ')
		x_type = int(x_type)
		if (x_type == 1):
			uid = self._read_book_id()
			self.__controller.book.delete_id(uid)
		elif (x_type == 2):
			title = self._read_book_title()
			self.__controller.book.delete_title(title)
		elif (x_type == 3):
			author = self._read_book_author()
			self.__controller.book.delete_author(author)

	def _read_categ(self, option):
		"""Citeste categoria optiunii."""
		suboption = None
		while (suboption != self.__exit_suboption):
			self.show_categ_menu()
			suboption = input('Introduceti categoria: ')
			try:
				if (suboption != self.__exit_suboption):
					self.__controller.take_suboption(suboption)
					suboption = int(suboption)
					if (suboption == 1):
						if (option == 1):
							self._read_book()
						elif (option == 2):
							self._read_x_categ_book('stergere')
						elif (option == 3):
							self._read_x_categ_book()
						elif (option == 7):
							self.__controller.book.display()
					elif (suboption == 2):
						if (option == 1):
							self._read_client()
						elif (option == 2):
							self._read_x_categ_client('stergere')
						elif (option == 3):
							self._read_x_categ_client()
						elif (option == 7):
							self.__controller.client.display()
					suboption = self.__exit_suboption
			except ValueError as err:
				print(err.args[0])

	def read_option(self):
		"""Citeste optiunea."""
		option = None
		while (option != self.__exit_option):
			self.show_menu()
			option = input('Introduceti optiunea: ')
			try:
				self.__controller.take_option(option)
				option = int(option)			
				if (option == 1):
					self._read_categ(option)
				elif (option == 2):
					self._read_categ(option)
				elif (option == 3):
					self._read_categ(option)
				elif (option == 4):
					self._read_categ(option)
				elif (option == 7):
					self._read_categ(option)
			except ValueError as err:
				print(err.args[0])
