class UI(object):
	"""docstring for UI"""

	def __init__(self, controller, client_controller, book_controller):
		self.__exit_option = 8;
		self.__exit_suboption = 3;
		self.__controller = controller
		self.__client_controller = client_controller
		self.__book_controller = book_controller

	def show_menu(self):
		"""Afiseaza meniul."""
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
		"""Afiseaza categoriile."""
		print('1. Carte.')
		print('2. Client.')
		print('3. Inapoi.')

	def _read_book(self):
		"""Citeste datele unei carti."""
		title = input('Introduceti titlul: ')
		description = input('Introduceti descrierea: ')
		author = input('Introduceti autorul: ')
		try:
			self.__book_controller.add(title, description, author)
		except ValueError as err:
			print(err.args[0])

	def _read_book_id(self):
		"""Citeste id-ul pentru carte."""
		uid = input('Id: ')
		return uid

	def _read_book_title(self):
		"""Citeste titlul pentru carte."""
		title = input('Titlu: ')
		return title

	def _read_book_description(self):
		"""Citeste descrierea pentru carte."""
		description = input('Descrierea: ')
		return description

	def _read_book_author(self):
		"""Citeste autorul pentru carte."""
		author = input ('Author: ')
		return author

	def _read_client_id(self):
		"""Citeste id-ul pentru client."""
		uid = input('Id: ')
		return uid

	def _read_client_name(self):
		"""Citeste numele pentru client."""
		name = input('Nume: ')
		return name

	def _read_client_cnp(self):
		"""Citeste cnp-ul pentru client."""
		cnp = input ('CNP: ')
		return cnp


	def _read_client(self):
		"""Citeste datele unui client."""
		name = input('Introduceti numele: ')
		cnp = input('Introduceti CNP-ul: ')
		try:
			self.__client_controller.add(name, cnp)
		except ValueError as err:
			print(err.args[0])

	def show_x_menu_book(self):
		"""Afiseaza categoriile pentru lucrul cu obiectul carte."""
		print('1. Id.')
		print('2. Titlu.')
		print('3. Autor.')
		print('4. Inapoi.')

	def show_x_menu_client(self):
		"""Afiseaza categoriile pentru lucrul cu obiectul client."""
		print('1. Id.')
		print('2. Nume.')
		print('3. CNP.')
		print('4. Inapoi.')

	def read_categ_book_delete(self):
		"""Citeste categoriile pentru stergerea unei carti"""
		self.show_x_menu_book()
		x_type = input('Introduceti tipul pentru stergere: ')
		try:
			x_type = int(x_type)
			if (x_type == 1):
				uid = self._read_book_id()
				self.__book_controller.delete_id(uid)
			elif (x_type == 2):
				title = self._read_book_title()
				self.__book_controller.delete_title(title)
			elif (x_type == 3):
				author = self._read_book_author()
				self.__book_controller.delete_author(author)
		except ValueError:
			print('Optiune invalida.')

	def read_categ_book_edit(self):
		"""Citeste categoriile pentru modificarea unei carti"""
		try:
			uid = self._read_book_id()
			pos = self.__book_controller.check_uid(uid)
			if (pos != -1):
				print('Actualizare...')
				title = self._read_book_title()
				description = self._read_book_description()
				author = self._read_book_author()
				try:
					self.__book_controller.edit_uid(pos, title, description, author)
				except ValueError as err:
					print(err.args[0])
			else:
				print('Cartea nu exista.')
		except ValueError:
			print('Id invalid.')

	def read_categ_client_delete(self):
		"""Citeste categoriile pentru stergerea unui client"""
		self.show_x_menu_client()
		x_type = input('Introduceti tipul pentru stergere: ')
		try:
			x_type = int(x_type)
			if (x_type == 1):
				uid = self._read_client_id()
				self.__client_controller.delete_id(uid)
			elif (x_type == 2):
				name = self._read_client_name()
				self.__client_controller.delete_name(name)
			elif (x_type == 3):
				cnp = self._read_client_cnp()
				self.__client_controller.delete_cnp(cnp)
		except ValueError:
			print("Optiune invalida.")


	def __display_clients(self):
		"""Afiseaza clienti."""
		items = self.__client_controller.display()
		print("\n" + '-------=======-------')
		for item in items:
			print(item, end="")

	def __display_books(self):
		"""Afiseaza carti."""
		items = self.__book_controller.display()
		print("\n" + '-------=======-------')
		for item in items:
			print(item, end="")

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
							#Citeste cartea pentru adaugare.
						elif (option == 2):
							self.read_categ_book_delete()
						elif (option == 3):
							self.read_categ_book_edit()
							pass
						elif (option == 4):
							pass
						elif (option == 7):
							self.__display_books()
					elif (suboption == 2):
						if (option == 1):
							self._read_client()
							#Citeste clientul pentru adaugare.
						elif (option == 2):
							self.read_categ_client_delete()
						elif (option == 3):
							# self.read_categ_client_edit()
							pass
						elif (option == 4):
							pass
						elif (option == 7):
							self.__display_clients()
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
