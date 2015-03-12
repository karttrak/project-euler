

class Queue:
	
	def __init__(self, s = -1):

		self.q = []
		self.capacity = s


	def __str__(self):

		return str(self.q)


	def __iter__(self):

		return iter(self.q)


	def __len__(self):

		return len(self.q)


	def push(self, obj):

		if len(self.q) == self.capacity:

			self.pop()

		self.q.append(obj)


	def pop(self):

		return self.q.pop(0)


	def peek(self):

		return self.q[0]


	def to_list(self):

		return self.q


def test_queue():

	q = Queue(4)

	for i in range(10):
		q.push(i)
		print(q)


if __name__ == '__main__':

	test_queue()