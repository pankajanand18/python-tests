intputs=["0123456789","0123456789a"]

def verifyString(input):
	for i in xrange(len(input)):
		try:
			if i is not int(input[i]):
				return False
		except Exception:
			return False

		
	return True


for input in intputs:
	print verifyString(input)

