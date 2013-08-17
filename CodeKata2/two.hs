import Test.QuickCheck
import Data.Array

--Very new to Haskell, so not sure this is optimum way to do it
--As docs suggest, getting element from list on index based is expensive
binarySearch :: Array a b -> Int -> Int
binarySearch inputList elemToSearch = binarySearchRecursive inputList elemToSearch 0 (length(inputList) - 1)
binarySearchRecursive [] _ _ _ = -1
binarySearchRecursive inputList elemToSearch i j | i > j = -1
                                | (inputList ! mid) == elemToSearch = mid
								| (inputList ! mid) < elemToSearch = binarySearchRecursive inputList elemToSearch (mid + 1) j 
							    | otherwise = binarySearchRecursive inputList elemToSearch i (mid - 1)
								where mid = ((i + j) `div` 2)
case0 = []
case1 = [1]
case2 = [1, 3, 5]
case3 = [1, 3, 5, 7]

prop_binarySearch methodName = methodName case0 0 0 3 == -1 
                            && methodName case1 0 0 3 == -1
							&& methodName case1 1 1 1 == 0
							&& methodName case2 1 == 0
							&& methodName case2 3 == 1
							&& methodName case2 5 == 2
							&& methodName case2 0 == -1
							&& methodName case2 2 == -1
							&& methodName case2 4 == -1
							&& methodName case2 6 == -1
							&& methodName case3 1 == 0
						    && methodName case3 3 == 1
						    && methodName case3 5 == 2
						    && methodName case3 7 == 3
						    && methodName case3 0 == -1
						    && methodName case3 2 == -1
						    && methodName case3 4 == -1
						    && methodName case3 6 == -1
						    && methodName case3 8 == -1	

--quickcheck message of 100 cases passed is misleading
--may need to write own unit test method
main = quickCheck(prop_binarySearch binarySearch)
