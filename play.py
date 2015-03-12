from lib import sorting_hat
unsorted = []

num = input("")

while(num != '..'):

	unsorted.append(int(num))
	num = input("")


print("\nOriginal list...")
print(unsorted)
print("\nSorted list...")
print(sorting_hat.quicksort(unsorted))