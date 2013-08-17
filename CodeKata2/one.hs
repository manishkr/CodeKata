module Main where

linearSearch :: [Int] -> Int -> Int
linearSearch list elem = linearSearchIndex list elem 0
linearSearchIndex [] _ _ = -1
linearSearchIndex (x : xs) elem i | x == elem = i
							      | otherwise = linearSearchIndex xs elem (i + 1)

myList = [1, 2, 3, 6, 8]

main :: IO()
main = print (linearSearch myList 2)
