class Menu(object):
	"""docstring for Menu"""

	def __init__(self, controller, client_controller, book_controller, borrow_controller):
		self.__exit_option = 8;
		self.__exit_suboption = 3;
		self.__controller = controller
		self.__client_controller = client_controller
		self.__book_controller = book_controller
		self.__borrow_controller = borrow_controller

	def print_nice(self, alist):
		print("\n" + '-------=======-------')
		for item in alist:
			print(item, end='')

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

	def read_book_add(self):
		"""Citeste datele unei carti."""
		title = self._read_book_title()
		description = self._read_book_description()
		author = self._read_book_author()
		try:
			return self.__book_controller.add(title, description, author)
		except ValueError as err:
			print(err.args[0])
			return (True)

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

	def read_client_add(self):
		"""Citeste datele unui client."""
		name = self._read_client_name()
		cnp = self._read_client_cnp()
		try:
			return self.__client_controller.add(name, cnp)
		except ValueError as err:
			print(err.args[0])
			return True

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
				if (self.__borrow_controller.check_if_exists_book(uid)):
					print('Cartea este imprumutata.')
				else:
					self.__book_controller.delete_id(uid)
			elif (x_type == 2):
				title = self._read_book_title()
				to_delete = True
				bk_obj = self.__book_controller.get_objs_from_title(title)
				for item in bk_obj:
					if (self.__borrow_controller.check_if_exists_book(item.getUid())):
						print('Cartea ' + str(item.getUid()) + ' este imprumutata.')
						to_delete = False
				if (to_delete):
					self.__book_controller.delete_title(title)
			elif (x_type == 3):
				author = self._read_book_author()
				to_delete = True
				bk_obj = self.__book_controller.get_objs_from_author(author)
				for item in bk_obj:
					if (self.__borrow_controller.check_if_exists_book(item.getUid())):
						print('Cartea ' + str(item.getUid()) + ' este imprumutata.')
						to_delete = False
				if (to_delete):
					self.__book_controller.delete_author(author)
			elif (x_type > 4):
				raise ValueError
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
				if (self.__borrow_controller.check_if_exists_client(uid)):
					print('Clientul are carti nereturnate.')
				else:
					self.__client_controller.delete_id(uid)
			elif (x_type == 2):
				to_delete = True
				name = self._read_client_name()
				cl_obj = self.__client_controller.get_objs_from_name(name)
				for item in cl_obj:
					if (self.__borrow_controller.check_if_exists_client(item.getUid())):
						print('Clientul ' + str(item.getUid()) + ' are carti nereturnate.')
						to_delete = False
				if (to_delete):
					self.__client_controller.delete_name(name)
			elif (x_type == 3):
				cnp = self._read_client_cnp()
				cl_obj = self.__client_controller.get_obj_from_cnp(cnp)
				if (self.__borrow_controller.check_if_exists_client(cl_obj.getUid())):
					print('Clientul are carti nereturnate.')
				else:
					self.__client_controller.delete_cnp(cnp)
			elif (x_type > 4):
				raise ValueError
		except ValueError:
			print("Optiune invalida.")

	def read_categ_client_edit(self):
		"""Citeste categoriile pentru modificarea unui client"""
		try:
			uid = self._read_client_id()
			pos = self.__client_controller.check_uid(uid)
			if (pos != -1):
				print('Actualizare...')
				name = self._read_client_name()
				cnp = self._read_client_cnp()
				try:
					self.__client_controller.edit_uid(pos, name, cnp)
				except ValueError as err:
					print(err.args[0])
			else:
				print('Clientul nu exista.')
		except ValueError:
			print('Id invalid.')

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

	def read_categ_client_search(self):
		self.show_x_menu_client()
		opt = input('Introduceti categoria: ')
		try:
			self.__controller.take_x_suboption(opt)
			opt = int(opt)
			if (opt == 1):
				uid = self._read_client_id()
				self.print_nice(self.__client_controller.search(uid, 'Uid'))
			elif (opt == 2):
				name = self._read_client_name()
				self.print_nice(self.__client_controller.search(name, 'Name'))
			elif (opt == 3):
				cnp = self._read_client_id()
				self.print_nice(self.__client_controller.search(cnp, 'CNP'))
		except ValueError as err:
			print(err.args[0])

	def read_categ_book_search(self):
		self.show_x_menu_book()
		opt = input('Introduceti categoria: ')
		try:
			self.__controller.take_x_suboption(opt)
			opt = int(opt)
			if (opt == 1):
				uid = self._read_book_id()
				self.print_nice(self.__book_controller.search(uid, 'Uid'))
			elif (opt == 2):
				title = self._read_book_title()
				self.print_nice(self.__book_controller.search(title, 'Title'))
			elif (opt == 3):
				author = self._read_book_author()
				self.print_nice(self.__book_controller.search(author, 'Author'))
		except ValueError as err:
			print(err.args[0])

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
							if (not self.read_book_add()):
								print('Cartea exista deja.')
							#Citeste cartea pentru adaugare.
						elif (option == 2):
							self.read_categ_book_delete()
						elif (option == 3):
							self.read_categ_book_edit()
						elif (option == 4):
							self.read_categ_book_search()
						elif (option == 7):
							self.__display_books()
					elif (suboption == 2):
						if (option == 1):
							if (not self.read_client_add()):
								return ('Clientul exista deja.')
							#Citeste clientul pentru adaugare.
						elif (option == 2):
							self.read_categ_client_delete()
						elif (option == 3):
							self.read_categ_client_edit_submenu()
						elif (option == 4):
							self.read_categ_client_search()
						elif (option == 7):
							self.__display_clients()
					suboption = self.__exit_suboption
			except ValueError as err:
				print(err.args[0])

	def show_menu_client_edit_submenu(self):
		print('1. Id.')
		print('2. CNP.')
		print('3. Inapoi.')

	def read_categ_client_edit_submenu(self):
		self.show_menu_client_edit_submenu()
		opt = input('Introduceti categoria: ')
		try:
			self.__controller.take_suboption(opt)
			opt = int(opt)
			pos = -1
			if (opt == 1 or opt == 2):
				if (opt == 1):
					uid = self._read_client_id()
					pos = self.__client_controller.check_uid(uid)
				elif (opt == 2):
					cnp = self._read_client_cnp()
					pos = self.__client_controller.check_cnp(cnp)
				if (pos != -1):
					print('Actualizare...')
					name = self._read_client_name()
					cnp = self._read_client_cnp()
					self.__client_controller.edit(pos, name, cnp)
				else:
					print('Clientul nu exista.')
		except ValueError as err:
			print (err.args[0])

	def borrow_return(self):
		print('Clientul care va imprumuta/returna cartea. (ID)')
		uid_c = self._read_client_id()
		print('Cartea care va fi imprumutata/returnata. (ID)')
		uid_b = self._read_book_id()
		if (self.__book_controller.check_uid(uid_b) != -1 and
			self.__client_controller.check_uid(uid_c) != -1):
			try:
				print(self.__borrow_controller.add_remove(uid_c, uid_b))
			except ValueError as err:
				print(err.args[0])
		else:
			print('Client sau carte inexistent/a.')

	def show_reports_menu(self):
		print('1. Cele mai inchiriate carti.')
		print('2. Clienti cu carti inchiriate.')
		print('3. Primi 20% dintre cei mai activi clienti (nume client si numarul de carti inchiriate)')
		print('4. Inapoi.')

	def most_borrow_report(self):
		print("\n" + '-------=======-------')
		how_many_books = 5
		for item in self.__borrow_controller.getReverseListBooks():
			if (how_many_books > 0):
				bk_obj = self.__book_controller.get_obj_from_id(item['id'])
				print(bk_obj, end='')
				how_many_books -= 1
			else:
				break

	def most_client_report_order_name(self):
		client_list = self.__borrow_controller.getClientIds()
		client_list = self.__client_controller.getListFromIdsOrderName(client_list)
		print("\n" + '-------=======-------')
		for client in client_list:
			print(client, end='')

	def most_client_report_order_books(self):
		client_list = self.__borrow_controller.getReverseListClients()
		client_list = self.__client_controller.getListFromIdsOrderBooks(client_list)
		print("\n" + '-------=======-------')
		for client in client_list:
			print(client, end='')

	def most_client_report(self):
		print('1. Nume.')
		print('2. Numarul de carti inchiriate.')
		print('3. Inapoi.')
		option = input('Ordonat dupa: ')
		try:
			self.__controller.take_suboption(option)
			option = int(option)
			if (option == 1):
				self.most_client_report_order_name()
			elif (option == 2):
				self.most_client_report_order_books()
		except ValueError as err:
			print(err.args[0])

	def read_reports(self):
		self.show_reports_menu()
		option = input('Introduceti optinea: ')
		try:
			self.__controller.take_x_suboption(option)
			option = int(option)
			if (option == 1):
				self.most_borrow_report()
			elif (option == 2):
				self.most_client_report()
			elif (option == 3):
				self.first_20_report()
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
				elif (option == 5):
					self.borrow_return()
				elif (option == 6):
					self.read_reports()
				elif (option == 7):
					self._read_categ(option)
			except ValueError as err:
				print(err.args[0])
