
class Queue:
	
	def __init__(self, s = -1):

		self.q = []
		self.capacity = s


	def __str__(self):

		return str(self.q)


	def __repr__(self):

		return str(self)


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


class Set:

	# Initialize the set object
	def __init__(self):
		
		self.l = []

		return None

	# Adds an item to the set unless it is a duplicate. Returns False if nothing is added.
	def add(self, item):

		if item not in self:
			self.l.append(item)
			return True

		return False

	# Adds all elements in the list to the set except duplicates. Returns False if nothing is added.
	def addList(self, list2):

		itemAdded = False

		for item in list2:
			itemAdded = self.add(item) or itemAdded

		return itemAdded

	# Defines how the set is printed
	def __str__(self):

		return '<' + str(self.l)[1:-1] + '>'

	# Returns the number of elements in the set
	def __len__(self):

		return len(self.l)

	# Creates an iterator for the set
	def __iter__(self):

		return iter(self.l)


	def __add__(self, set2):

		return self.union(set2)

	# Returns a set containing all the elements in the two passed sets.
	def union(self, set2):

		union = OurSet()

		union.addList(self)
		union.addList(set2)

		return union

	# Returns a set containing only the elements in both passed sets.
	def intersection(self, set2):

		intersection = OurSet()

		for item in self:
			if item in set2:
				intersection.add(item)

		return intersection


if __name__ == '__main__':

	test_queue()