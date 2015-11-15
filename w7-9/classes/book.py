class Book(object):
	"""docstring for Book"""
	def __init__(self, uid, title, description, author):
		self.__uid = uid
		self._title = title
		self._description = description
		self._author = author
		
	def __str__(self):
		str_ = '';
		str_ += 'Id: ' + str(self.__uid) + "\n"
		str_ += 'Titlu: "' + str(self._title) + "\"\n"
		str_ += 'Descriere: "' + str(self._description) + "\"\n"
		str_ += 'Autor: "' + str(self._author) + "\"\n"
		str_ += "-------=======-------\n"
		return str_

	def getUid(self):
		return self.__uid

	def getTitle(self):
		return self._title

	def setTitle(self, new_title):
		self._title = new_title

	def getDescription(self):
		return self._description

	def setDescription(self, new_description):
		self._description  = new_description

	def getAuthor(self):
		return self._author
