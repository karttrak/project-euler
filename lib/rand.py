import random

def rand_nums(size, lower_bound = 0, upper_bound = 100):

	for i in range(size):

		print(random.randint(lower_bound, upper_bound))


if __name__ == '__main__':

	size = random.randint(0, 50)
	lower_bound = random.randint(-100, -10)
	upper_bound = random.randint(10, 100)

	rand_nums(size, lower_bound, upper_bound)

	print("..")