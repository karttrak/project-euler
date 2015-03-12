from lib import queue

def get_product(q):

	product = 1

	for x in q:

		product *= int(x)

	return product


def get_contents(q):

	l = []

	for x in q:

		l.append(x)

	return l


q = queue.Queue(13)

maximum = (0,0)

read_in = input("")

for x in read_in:

	q.push(x)

	product = get_product(q)

	if product > maximum[0]:

		maximum = (product, get_contents(q))

print(maximum)