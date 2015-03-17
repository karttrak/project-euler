from lib import primes

# sum_primes = 2

# for num in range(3, 2000000, 2):

# 	if primes.is_prime(num):

# 		sum_primes += num

# print(sum_primes)

l = primes.prime_list_up_to(2000000)
s=0
for p in l:

	s += p

print(s)