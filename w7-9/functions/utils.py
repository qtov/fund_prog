import re

def getMaxUid(type_):
	max_uid = 0
	try:
		repo = open("repositories/" + type_ + "_repository", "r")
	except IOError:
		return max_uid
	try:
		for line in repo.readlines():
			uid = re.match("[a-z:\s]+(\d+)", line, re.I)
			if (int(uid.group(1)) > max_uid):
				max_uid = int(uid.group(1))
	except AttributeError:
		return max_uid
	repo.close()
	return max_uid
