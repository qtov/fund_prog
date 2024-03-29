class Client(object):
	"""docstring for Client"""
	def __init__(self, uid, name, CNP, points):
		self.__uid = uid
		self._name = name
		self.__CNP = CNP
		self.__points = points
	
	def __str__(self):
		str_ = '';
		str_ += 'Id: ' + str(self.__uid) + "\n"
		str_ += 'Nume: \"' + str(self._name) + "\"\n"
		str_ += 'CNP: \"' + str(self.__CNP) + "\"\n"
		str_ += 'Puncte: ' + str(self.__points) + "\n"
		str_ += "-------=======-------\n"
		return str_

	def getUid(self):
		return self.__uid

	def getPoints(self):
		return self.__points

	def incBorrow(self):
		self.__points += 1

	def getName(self):
		return self._name

	def setName(self, new_name):
		self._name = new_name

	def getCNP(self):
		return self.__CNP

	def setCNP(self, cnp):
		self.__CNP = cnp

	def __eq__(self, client):
		if (self.getCNP() == client.getCNP()):
			return (True)
		else:
			return (False)
