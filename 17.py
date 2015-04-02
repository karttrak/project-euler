one 	= {}		# ones place
one[0]	= ""
one[1]	= "one"
one[2]	= "two"
one[3]	= "three"
one[4]	= "four"
one[5]	= "five"
one[6]	= "six"
one[7]	= "seven"
one[8]	= "eight"
one[9]	= "nine"

teen	= {}		# teens
teen[0]	= "ten"
teen[1]	= "eleven"
teen[2]	= "twelve"
teen[3]	= "thirteen"
teen[4]	= "fourteen"
teen[5]	= "fifteen"
teen[6]	= "sixteen"
teen[7]	= "seventeen"
teen[8]	= "eighteen"
teen[9]	= "nineteen"

ten		= {}		# tens place
ten[0]	= ""
ten[1]	= ""		# teens
ten[2]	= "twenty"
ten[3]	= "thirty"
ten[4]	= "forty"
ten[5]	= "fifty"
ten[6]	= "sixty"
ten[7]	= "seventy"
ten[8]	= "eighty"
ten[9]	= "ninety"


def number_length(n):

	ones 		= int(n/1) % 10
	tens 		= int(n/10) % 10
	hundreds 	= int(n/100) % 10
	thousands 	= int(n/1000) % 10

	number_string = ""
	if thousands:
		number_string += one[thousands] + "thousand"
	if hundreds:
		number_string += one[hundreds] + "hundred"
	if (ones or tens) and (hundreds or thousands):
		number_string += "and"
	number_string += teen[ones] if tens == 1 else (ten[tens] + one[ones])

	return number_string


summation = 0

for j in range(1001):

	summation += len(number_length(j))
	# print(str(j) + ": " + number_length(j))

print(summation)