

def get_factors(num):

	factors = []

	for j in range(1, int(num/2+1)):

		if num % j == 0:

			factors.append(j)

		if j > 100 and len(factors) < 50:

			return []

	factors.append(num)

	return factors


factor_count = 0
j = 1

while factor_count < 500:

	triangle_sum = 0

	for k in range(1, j+1):

		triangle_sum += k

	if triangle_sum % 2 == 0:

		factor_count = len(get_factors(triangle_sum))

		if factor_count > 100:

			print(str(triangle_sum) + " " + str(factor_count))
	
	j += 1

print(get_factors(76576500))