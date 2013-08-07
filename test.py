def pow(num, e):
	"""
	calculate the pow of num
	"""

	if e < 0:
		return -1
	base = 1
	for i in range(e):
		base *= num
	return base

def add(a ,b):
	"""
	this the the adding function
	"""
	return a+b

def minus(a,b):
	return a-b

def main():
	num = 2
	e = 2
	print pow(num, e)
	print add(num ,e)
	print minus(3,4)

if __name__=="__main__":
	main()