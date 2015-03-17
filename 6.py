def diff(num):
	
	sum_of_sq = 0
	sq_of_sum = 0

	for i in range(num+1):

		sum_of_sq += pow(i, 2)
		sq_of_sum += i

	sq_of_sum = pow(sq_of_sum, 2)

	return sq_of_sum - sum_of_sq


print(diff(100))