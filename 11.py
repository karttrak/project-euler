
def check_right(grid, i, j):

	product = 1

	for k in grid[i][j:j+4]:

		product *= k

	return product


def check_down_right(grid, i, j):

	product = 1
	i2 = 4

	if i+i2 > len(grid):

		i2 = len(grid) - i

	if j+i2 > len(grid[i]):

		i2 = len(grid[i]) - j

	for k in range(i2):

		product *= grid[i+k][j+k]

	return product


def check_down(grid, i, j):

	product = 1
	i2 = 4

	if i+i2 > len(grid):

		i2 = len(grid) - i

	for k in range(i2):

		product *= grid[i+k][j]

	return product


def check_down_left(grid, i, j):

	product = 1
	i2 = 4

	if i+i2 > len(grid):

		i2 = len(grid) - i

	if j-i2 < 0:

		i2 = j

	for k in range(i2):

		product *= grid[i+k][j-k]

	return product


f = open('input.txt', 'r')

grid = []

for line in f:

	l = line.split(" ")
	line = []

	for num in l:

		line.append(int(num))

	grid.append(line)

max_product = 0

for j in range(len(grid)):

	for k in range(len(grid[j])):

		right = check_right(grid, j, k)
		down_right = check_down_right(grid, j, k)
		down = check_down(grid, j, k)
		down_left = check_down_left(grid, j, k)

		product = max(right, down_right, down, down_left)

		if product > max_product:

			max_product = product


# for k in grid[1:3]:

# 	print(k)
print(max_product)

		