
class Point:

	def __init__(self, x=0, y=0):

		self.x = x
		self.y = y


	def __str__(self):

		return '(' + str(self.x) + ', ' + str(self.y) + ')'


	def __repr__(self):

		return str(self)


	def getX(self):

		return self.x


	def getY(self):

		return self.y


	def __eq__(self, other):

		return self.x == other.x and self.y == other.y


if __name__ == '__main__':

	p = Point(2, 4)
	print(p)