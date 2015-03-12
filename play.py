from lib import sorting_hat

def sort_ints():

	unsorted = []

	num = input("")

	while(num != '..'):

		unsorted.append(int(num))
		num = input("")


	print("\nOriginal list...")
	print(unsorted)
	print("\nSorted list...")
	print(sorting_hat.quicksort(unsorted))


def sort_letters(sentence):

	str_list = sentence.split(' ')

	out = ""

	for s in str_list:

		s = sorting_hat.quicksort(s)

		for c in s:

			out += c

		out += " "

	return out


if __name__ == '__main__':

	# sort_ints()

	inp = input("")

	while inp != "..":

		print(sort_letters(inp))
		inp = input("")