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




__author__ = 'Kyle Thornburgh'

import unittest
from hw2_set import OurSet

class TestSet(unittest.TestCase):

    def setUp(self):
        self.emptySet = OurSet()
        self.s1 = OurSet()
        self.s2 = OurSet()

        self.s1.addList([3, '4', 4, 9, 1])
        self.s2.addList([9, 99, 'pizza', '4', 0, 1])


    def test_union(self):
        """S4: Test union of two sets"""
        self.assertEqual(str(self.s1.union(self.s2)), '<3, \'4\', 4, 9, 1, 99, \'pizza\', 0>', 'Should return set containing all items from both sets')
        self.assertEqual(str(self.s2 + self.s1), '<9, 99, \'pizza\', \'4\', 0, 1, 3, 4>', 'Should return set containing all items from both sets')
        self.assertEqual(str(self.s1), '<3, \'4\', 4, 9, 1>', 'Original set contents should remain unaltered')
        self.assertEqual(str(self.s2), '<9, 99, \'pizza\', \'4\', 0, 1>', 'Original set contents should remain unaltered')


    def test_union_empty(self):
        """S5: Test union with an empty set"""
        self.assertEqual(str(self.s1 + self.emptySet), '<3, \'4\', 4, 9, 1>', 'Should return same contents as the filled set')
        self.assertEqual(str(self.emptySet + self.s2), '<9, 99, \'pizza\', \'4\', 0, 1>', 'Should return same contents as the filled set')
        

    def test_union_self(self):
        """S6: Test union with itself"""
        self.assertEqual(str(self.s1 + self.s1), '<3, \'4\', 4, 9, 1>', 'Should return same contents as either input sets without duplicates')
        self.assertEqual(str(self.s2 + self.s2), '<9, 99, \'pizza\', \'4\', 0, 1>', 'Should return same contents as either input sets without duplicates')


    def test_intersection(self):
        """S7: Test intersection of two sets"""
        self.assertEqual(str(self.s1.intersection(self.s2)), '<\'4\', 9, 1>', 'Should return set containing all the common items between the two given sets')
        self.assertEqual(str(self.s2.intersection(self.s1)), '<9, \'4\', 1>', 'Should return set containing all the common items between the two given sets, but in different order than before')
        self.assertEqual(str(self.s1), '<3, \'4\', 4, 9, 1>', 'Initial set contents should be unaltered')
        self.assertEqual(str(self.s2), '<9, 99, \'pizza\', \'4\', 0, 1>', 'Initial set contents should be unaltered')


    def test_intersection_empty(self):
        """S8: Test intersection with an empty set"""
        self.assertEqual(str(self.s1.intersection(self.emptySet)), '<>', 'Any intersection with an empty set should return an empty set')
        self.assertEqual(str(self.emptySet.intersection(self.s2)), '<>', 'Any intersection with an empty set should return an empty set')
        

    def test_intersection_self(self):
        """S9: Test intersection with itself"""
        self.assertEqual(str(self.s1.intersection(self.s1)), '<3, \'4\', 4, 9, 1>', 'Any intersection of a set with itself returns itself')
        self.assertEqual(str(self.s2.intersection(self.s2)), '<9, 99, \'pizza\', \'4\', 0, 1>', 'Any intersection of a set with itself returns itself')


    def test_union_intersection(self):
        """S10: Test union and intersection methods combined"""
        self.assertEqual(str((self.s1 + self.s2).intersection(self.s1)), '<3, \'4\', 4, 9, 1>')
        self.assertEqual(str((self.s2 + self.s1).intersection(self.s2)), '<9, 99, \'pizza\', \'4\', 0, 1>')
        self.assertEqual(str((self.s1 + self.s2).intersection(self.s2)), '<\'4\', 9, 1, 99, \'pizza\', 0>')
        self.assertEqual(str((self.s2 + self.s1).intersection(self.s1)), '<9, \'4\', 1, 3, 4>')


if __name__ == '__main__':

    unittest.main()
