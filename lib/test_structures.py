import structures
import unittest

def test_queue():

	q = Queue(4)

	for i in range(10):
		q.push(i)
		print(q)


def test_set():

	s = structures.Set()
	s.add(3)
	s.add(3)
	s.add(3)
	s.addList([1, 2, 3])
	print(s)


if __name__ == '__main__':

	test_set()