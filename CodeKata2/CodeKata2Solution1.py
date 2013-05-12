#!/usr/bin/python3
import unittest

""" Class to test search in sorted
"""
class SearchInSortedTest(unittest.TestCase):		
	def setUp(self):
		self.Case0 = []
		self.Case1 = [1]
		self.Case2 = [1, 3, 5]
		self.Case3 = [1, 3, 5, 7]
		self.Case4 = [2, 2, 2, 2]
		self.Case5 = [2, 2, 2, 5, 5]
		
	def testLinearSearch(self):
		print("Testing Linear Search")
		self.DoTestSearchInSorted(LinearSearchInSorted)
		
	def testBinarySearch(self):
		print("Testing Binary Search")
		self.DoTestSearchInSorted(BinarySearchInSorted, False)
		
	def testBinarySearchStable(self):
		print("Testing Binary Search Stable")
		self.DoTestSearchInSorted(BinarySearchInSortedStable)
		
	def DoTestSearchInSorted(self, methodName, stable=True):
		print("Executing Case0")
		self.assertEqual(-1, methodName(self.Case0, 3))
		#
		print("Executing Case1")
		self.assertEqual(-1, methodName(self.Case1, 3))
		self.assertEqual(0, methodName(self.Case1, 1))
		#
		print("Executing Case2")
		self.assertEqual(0, methodName(self.Case2, 1))
		self.assertEqual(1, methodName(self.Case2, 3))
		self.assertEqual(2, methodName(self.Case2, 5))
		self.assertEqual(-1, methodName(self.Case2, 0))
		self.assertEqual(-1, methodName(self.Case2, 2))
		self.assertEqual(-1, methodName(self.Case2, 4))
		self.assertEqual(-1, methodName(self.Case2, 6))
		#
		print("Executing Case3")
		self.assertEqual(0, methodName(self.Case3, 1))
		self.assertEqual(1, methodName(self.Case3, 3))
		self.assertEqual(2, methodName(self.Case3, 5))
		self.assertEqual(3, methodName(self.Case3, 7))
		self.assertEqual(-1, methodName(self.Case3, 0))
		self.assertEqual(-1, methodName(self.Case3, 2))
		self.assertEqual(-1, methodName(self.Case3, 4))
		self.assertEqual(-1, methodName(self.Case3, 6))
		self.assertEqual(-1, methodName(self.Case3, 8))
		#
		if(True == stable):
			print("Executing Case4")
			self.assertEqual(0, methodName(self.Case4, 2))
			self.assertEqual(-1, methodName(self.Case4, 3))
			
			self.assertEqual(0, methodName(self.Case5, 2))
			self.assertEqual(3, methodName(self.Case5, 5))
		
"""
Best Case : O(1)
Average Case : O(n)
Worst Case : O(n)
"""		
def LinearSearchInSorted(inputArray, elementToSearch):
	index = -1
	size = len(inputArray)
	for i in range(size):
			if (elementToSearch == inputArray[i]):
				index = i
				break
	return index

"""
Best Case : O(1)
Average Case : O(logn)
Worst Case : O(n)
"""	
def BinarySearchInSorted(inputArray, elementToSearch):
	return BinarySearchRecursive(inputArray, elementToSearch, 0, len(inputArray) - 1)
	
def BinarySearchRecursive(inputArray, elementToSearch, startIndex, endIndex):
	if len(inputArray) < 1:
		return -1;
	
	if(endIndex < startIndex):
		return -1;
	
	mid = int((startIndex + endIndex) / 2)
	
	if(elementToSearch < inputArray[mid]):
		return BinarySearchRecursive(inputArray, elementToSearch, startIndex, mid - 1)
	elif elementToSearch == inputArray[mid]:
		return mid
	else:
		return BinarySearchRecursive(inputArray, elementToSearch, mid + 1, endIndex)
	
	return -1

"""
This is not a different solution, it is just stable version of BinarySearchInSorted
Best Case : O(1)
Average Case : O(logn)
Worst Case : O(n)
"""	
def BinarySearchInSortedStable(inputArray, elementToSearch):
	return BinarySearchRecursiveStable(inputArray, elementToSearch, 0, len(inputArray) - 1)

def BinarySearchRecursiveStable(inputArray, elementToSearch, startIndex, endIndex):
	if len(inputArray) < 1:
		return -1;
	
	if(endIndex < startIndex):
		return -1;
	
	mid = int((startIndex + endIndex) / 2)
	
	if(elementToSearch < inputArray[mid]):
		return BinarySearchRecursive(inputArray, elementToSearch, startIndex, mid - 1)
	elif elementToSearch == inputArray[mid]:
		#Get the lowest index of element which is repeated
		while((mid > startIndex) and (elementToSearch == inputArray[mid - 1])):
			mid = mid - 1;
			
		return mid
	else:
		return BinarySearchRecursive(inputArray, elementToSearch, mid + 1, endIndex)
	
	return -1	

if __name__ == '__main__':
	unittest.main()
