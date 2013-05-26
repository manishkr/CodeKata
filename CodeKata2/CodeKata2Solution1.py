#!/usr/bin/python3
import unittest

""" 
Problem : http://codekata.pragprog.com/2007/01/kata_two_karate.html
Class to test search in sorted
"""
class SearchInSortedTest(unittest.TestCase):		
	def setUp(self):
		self.Case0 = []
		self.Case1 = [1]
		self.Case2 = [1, 3, 5]
		self.Case3 = [1, 3, 5, 7]
		self.Case4 = [2, 2, 2, 2]
		self.Case5 = [2, 2, 2, 5, 5]
		
	def testBinarySearch(self):
		print("Testing Binary Search")
		self.DoTestSearchInSorted(BinarySearchInSorted, False)
		
	def testBinarySearchStable(self):
		print("Testing Binary Search Stable")
		self.DoTestSearchInSorted(BinarySearchInSortedStable)
	
	def testBinarySearchNonRecursive(self):
		print("Testing Binary Search Non Recursive")
		self.DoTestSearchInSorted(BinarySearchInSortedNonRecursive, False)
			
	def testBinarySearchViaSlice(self):
		print("Testing Binary Search Recursive via array slice")
		self.DoTestSearchInSorted(BinarySearchRecursiveViaSlice, False)	
			
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
Average Case : O(logn)
Worst Case : O(logn)
"""	
def BinarySearchInSorted(inputArray, elementToSearch):
	return BinarySearchRecursive(inputArray, elementToSearch, 0, len(inputArray) - 1)
	
def BinarySearchRecursive(inputArray, elementToSearch, startIndex, endIndex):
	index = -1
	
	if(startIndex <= endIndex):
		mid = int((startIndex + endIndex) / 2)
		
		if(elementToSearch < inputArray[mid]):
			index = BinarySearchRecursive(inputArray, elementToSearch, startIndex, mid - 1)
		elif(elementToSearch == inputArray[mid]):
			index = mid
		else:
			index = BinarySearchRecursive(inputArray, elementToSearch, mid + 1, endIndex)
	
	return index

"""
This is not a different solution, it is just stable version(lowest Index for repeated element)
 of BinarySearchInSorted
Best Case : O(1)
Average Case : O(logn)
Worst Case : O(logn)
"""	
def BinarySearchInSortedStable(inputArray, elementToSearch):
	return BinarySearchRecursiveStable(inputArray, elementToSearch, 0, len(inputArray) - 1)

def BinarySearchRecursiveStable(inputArray, elementToSearch, startIndex, endIndex):
	index = -1
	
	if(startIndex <= endIndex):	
		mid = int((startIndex + endIndex) / 2)
		
		if(elementToSearch < inputArray[mid]):
			index = BinarySearchRecursive(inputArray, elementToSearch, startIndex, mid - 1)
		elif elementToSearch == inputArray[mid]:
			#Get the lowest index of element which is repeated
			while((mid > startIndex) and (elementToSearch == inputArray[mid - 1])):
				mid = mid - 1
			index = mid
		else:
			index = BinarySearchRecursive(inputArray, elementToSearch, mid + 1, endIndex)
	
	return index	

"""
Best Case : O(1)
Average Case : O(logn)
Worst Case : O(logn)
"""	
def BinarySearchInSortedNonRecursive(inputArray, elementToSearch):
	startIndex = 0
	endIndex = len(inputArray) - 1
	
	index = -1
	
	while(startIndex <= endIndex):
		mid = int((startIndex + endIndex) / 2)
		
		if(elementToSearch == inputArray[mid]):
			index = mid
			break
		elif(elementToSearch < inputArray[mid]):
			endIndex = mid - 1
		else:
			startIndex = mid + 1
			
	return index

"""
As Python slicing copy the array and make new one, this need extra space and complexity due to copy
Although searching number of comparision will be same, but copying complexity will be in term of 
n/2 + n/4 + n/8...i.e. O(n)
"""
def BinarySearchRecursiveViaSlice(inputArray, elementToSearch):
	startIndex = 0
	endIndex = len(inputArray) - 1
	
	index = -1
	
	if(startIndex <= endIndex):
		mid = int((startIndex + endIndex) / 2)
		
		if(elementToSearch == inputArray[mid]):
			index = mid
		elif(elementToSearch < inputArray[mid]):
			index = BinarySearchRecursiveViaSlice(inputArray[startIndex : mid], elementToSearch)
		else:
			tempIndex = BinarySearchRecursiveViaSlice(inputArray[(mid + 1) : (endIndex + 1)], elementToSearch)
			if(tempIndex > -1):
				index  = mid + 1 + tempIndex
	
	return index
	
if __name__ == '__main__':
	unittest.main()
