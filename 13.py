
summation = 0

f = open('input.txt', 'r')

for line in f:

	summation += int(line)

print(str(summation)[:10])

f.close()