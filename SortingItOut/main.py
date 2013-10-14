import unittest
from SortFixedRangeNumbers import SortFixedRangeNumbers  
from SortChars import SortChars

class TestSorting(unittest.TestCase):
	def test_number_sorting_1(self):
		sorter = SortFixedRangeNumbers(0, 59)
		self.assertEqual([], sorter.get_sorted())
		sorter.add(20)
		self.assertEqual([20], sorter.get_sorted())	
		sorter.add(10)
		self.assertEqual([10, 20], sorter.get_sorted())
		sorter.add(30)
		self.assertEqual([10, 20, 30], sorter.get_sorted())
		sorter.add(10)
		self.assertEqual([10, 10, 20, 30], sorter.get_sorted())
	
	def test_number_sorting_2(self):
		sorter = SortFixedRangeNumbers(0, 25)
		self.assertEqual([], sorter.get_sorted())
		sorter.add(0)
		sorter.add(0)
		self.assertEqual([0, 0], sorter.get_sorted())
		sorter.add(1)
		sorter.add(2)
		self.assertEqual([0, 0, 1, 2], sorter.get_sorted())
		sorter.add(24)
		self.assertEqual([0, 0, 1, 2, 24], sorter.get_sorted())
		sorter.add(25)
		sorter.add(25)
		self.assertEqual([0, 0, 1, 2, 24, 25, 25], sorter.get_sorted())

	def test_char_sorting_1(self):
		sorter = SortChars()
		sorter.add("When not studying nuclear physics, Bambi likes to play beach volleyball.")
		self.assertEqual("aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsssstttuuvwyyyy", sorter.get_sorted())

if __name__ == '__main__':
	unittest.main()
