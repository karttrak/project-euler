
def fact(n):

	if n <= 2:

		return 2

	return n * fact(n-1)


fact = fact(100)
summation = 0

for c in str(fact):

	summation += int(c)

print(summation)
