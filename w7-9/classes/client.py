class Client(object):
	"""docstring for Client"""
	def __init__(self, uid, name, CNP):
		self.__uid = uid
		self._name = name
		self.__CNP = CNP
	
	def __str__(self):
		str_ = '';
		str_ += 'Id: ' + str(self.__uid) + "\n"
		str_ += 'Nume: ' + str(self._name) + "\n"
		str_ += 'CNP: ' + str(self.__CNP) + "\n"
		return str_

	def getUid(self):
		return self.__uid

	def getName(self):
		return self._name

	def setName(self, new_name):
		self._name = new_name

	def getCNP(self):
		return self.__CNP

	# def getAddress(self):
	# 	return self._address

	# def setAddress(self, new_address):
	# 	self._address = new_address
