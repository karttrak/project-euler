a = b = 1
evenFibSum = 0

while(a < 4000000):
	
	if a%2 == 0:
		evenFibSum += a

	tmp = a
	a = b
	b = a + tmp

print(evenFibSum)