
def fib(n):

	a = b = 1
	j = 1
	size = len(str(a))
	print(str(j) + ": " + str(size))

	while size != 1000:

		c = a+b
		a = b
		b = c

		size = len(str(a))
		j += 1

		print(str(j) + ": " + str(size))

fib(100)