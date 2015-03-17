def smallest_multiple(num):

	ans = 0
	i = num

	while True:

		for j in range(1, num+1):

			if i%j != 0:

				break

			elif j == num:

				return i

		i += num


print(smallest_multiple(20))