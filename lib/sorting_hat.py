def swap(l, a, b):

	temp = l[a]
	l[a] = l[b]
	l[b] = temp


def is_sorted(lst):

	for i in range(len(l)-1):

		if l[i] > l[i+1]:

			return False

	return True


def bubblesort(lst):

	l = []
	for i in range(len(lst)):
		l.append(lst[i])

	for j in range(len(l)-1):

		for i in range(len(l)-1):

			if l[i] > l[i+1]:

				swap(l, i, i+1)

	return l


def mergesort(l, i, j):

	if len(l) <= 1:

		return l

	elif len(l) <= 2:

		if l[i] > l[j]:

			swap(l, i, j)

		return l

	return mergesort(l, 0, j-1) + mergesort(l, j, len(l)-1)


def quicksort(lst):

	l = []
	for i in range(len(lst)):
		l.append(lst[i])

	if len(l) <= 1:

		return l

	pivot = 0
	end = len(l) - 1

	for x in range(end):

		if l[pivot+1] < l[pivot]:

			swap(l, pivot, pivot+1)
			pivot += 1

		else:

			swap(l, pivot+1, end)
			end -= 1

	return quicksort(l[:pivot]) + [l[pivot]] + quicksort(l[pivot+1:])


def test_sorts():

	l1 = ['a', 'f', 'g', 'b', 'c', 'q', 'a']
	l2 = [3]
	l3 = [1, 3]
	l4 = [5, 2]
	l5 = [6, 1, 78, 1, 0, -3]
	l6 = [1, 5, 6, 4, 87, 8, 1]
	l7 = [11, 5, 3, 1, 0, -1, -2, -5, -12]

	lists = [l1, l2, l3, l4, l5, l6, l7]

	for l in lists:

		sort = quicksort(l)
		print(str(l) + "\n" + str(sort) + "\n")


if __name__ == '__main__':

	test_sorts()