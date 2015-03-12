
def triplet():

	for a in range(1, 1000):

		for b in range(2, 1000):

			for c in range(3, 1000):

				if a + b + c == 1000:

					if pow(a, 2) + pow(b, 2) == pow(c, 2):

						print(str(a) + " + " + str(b) + " + " + str(c) + " = " + str(a+b+c))

						return str(a) + " + " + str(b) + " + " + str(c) + " = " + str(a+b+c)

		print(a)

print(triplet())