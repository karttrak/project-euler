import math

num_digits = 3
x = int(math.pow(11, num_digits-1))
y = int(math.pow(10, num_digits))
ans = 0

for i in range(x, y, 11):

	for j in range(x, y, 1):

		temp = i * j
		reverse = int(str(temp)[::-1])

		if temp == reverse and temp > ans:

			ans = temp

print(ans)