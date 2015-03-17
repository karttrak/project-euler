import math

def get_factors(num):

	factors = []

	for j in range(1, int(math.sqrt(num)+1)):

		if num % j == 0:

			factors.append(j)
			mirror = int(num/j)

			if mirror != j:

				factors.append(mirror)

		if j > 100 and len(factors) < 100:

			return []

	return factors


factor_count = 0
n = 1

while factor_count < 500:

	triangle_sum = int(n*(n+1)/2)

	if triangle_sum % 2 == 0:

		factor_count = len(get_factors(triangle_sum))

		if factor_count >= 300:

			print(str(triangle_sum) + " " + str(factor_count))
	
	n += 1