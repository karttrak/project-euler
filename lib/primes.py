import math

def is_prime(num):

	if num%2 == 0:

		return False

	lim = int(math.sqrt(num)) + 1

	for i in range(3, lim, 2):

		if num%i == 0:

			return False

	return True


def prime_factors(num):

	factors = []

	lim = int(math.sqrt(num)) + 1

	if lim%2 == 0:

		lim += 1

	for i in range(lim, 1, -2):

		if num%i == 0:

			if is_prime(i):

				factors.append(i)

	if num%2 == 0:

		factors.append(2)

	return factors


def prime_list_up_to(num):

	primes = [2]

	for i in range(3, num, 2):

		if (is_prime(i)):

			primes.append(i)

	return primes


def nth_prime(num):

	i = 1
	count = 1

	while count < num:

		i += 2

		if is_prime(i):

			count += 1

	return i


if __name__ == '__main__':

	# print(prime_factors(600851475143))
	# print(is_prime(600851475143))
	print(len(prime_list_up_to(100000)))