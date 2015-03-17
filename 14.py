def collatz(start):

	cur = start
	numbers = [start]

	while cur != 1:

		if cur < start:

			return counts[cur] + len(numbers)-1

		if cur%2 == 0:

			numbers.append(int(cur/2))

		else:

			numbers.append(3*cur + 1)

		cur = numbers[len(numbers)-1]

	return len(numbers)


counts = [0]

for j in range(1, 1000000):

	count = collatz(j)
	counts.append(count)

print(max(counts))
