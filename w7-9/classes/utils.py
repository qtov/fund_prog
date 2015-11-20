import re

class Utils(object):
	def getMaxUid(self, type_):
		"""Returneaza id-ul maxim gasit in fisier."""
		max_uid = 0
		try:
			repo = open("repositories/" + type_ + "_repository", "r")
		except IOError:
			return max_uid
		for line in repo.readlines():
			try:
				uid = re.match("Id:\s(\d+)", line, re.I)
				if (int(uid.group(1)) > max_uid):
					max_uid = int(uid.group(1))
			except AttributeError:
				pass
		repo.close()
		return max_uid
