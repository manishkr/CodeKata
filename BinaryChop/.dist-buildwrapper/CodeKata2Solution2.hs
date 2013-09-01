import Data.Array

binarySearch :: [Int] -> Int -> Int
binarySearch list elem = binarySearchIndex list elem 0 (length(list) - 1)
binarySearchIndex [] _ _ _ = -1
binarySearchIndex list elem i j | (list !! ((i + j) `div` 2)) == elem = ((i + j) `div` 2)
                                                                | (list !! ((i + j) `div` 2)) < elem = binarySearchIndex list elem (((i + j) `div` 2) + 1) j 
                                                            | otherwise = binarySearchIndex list elem i (((i +j) `div` 2) - 1)

myList = [1, 2, 3, 6, 8]

main :: IO()
main = print (binarySearch myList 2)
