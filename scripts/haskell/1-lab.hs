-- insertion sort

pop :: Num a => Int -> [a] -> (a, [a])
pop index arr = (val, res) where
  val = arr !! index
  res = search 0 arr
  search :: Num a => Int -> [a] -> [a]
  search i (x : xs) 
    | i == index = xs
    | otherwise = x : (i + 1) `search` xs
  
isEven :: (Integral a, Eq a, Ord a, Num a) => a -> Bool
isEven x = (x `mod` 2)  == 0

(%>) :: (Integral a, Eq a, Ord a, Num a) => a -> [a] -> [a]
(%>) val [] = [val]
(%>) val (x : xs)
  | isEven x = push
  | otherwise = val : x : xs
  where
    push
      | x >= val = val : x : xs
      | otherwise = x : val %> xs

($>) :: (Integral a, Eq a, Ord a, Num a) => a -> [a] -> [a]
($>) val [] = [val]
($>) val (x : xs)
  | isEven x = x : val $> xs
  | otherwise = push $ x : xs
  where
    push [] = [val]
    push (y : ys)
      | isEven y || y <= val = val : y : ys
      | otherwise = y : push ys

(&>) :: (Integral a, Eq a, Ord a, Num a) => a -> [a] -> [a]
(&>) val [] = [val]
(&>) val arr
  | isEven val = val %> arr
  | otherwise = val $> arr

insertion_sort ::(Integral a, Eq a, Ord a, Num a) => Int -> [a] -> [a]
insertion_sort index arr
  | index == length arr = arr
  | otherwise = sort
  where
    (val, rest) = index `pop` arr
    res = val &> rest
    sort = insertion_sort (index + 1) res

insertionSort :: (Integral a, Eq a, Ord a, Num a) => [a] -> [a]
insertionSort = insertion_sort 1 

main :: IO()
main = do
  let array = [30, 19, 9, 15, 55, 24, 3, 78, 46, 41]
  putStr "Input array:\n "
  print array
  putStr "Result (sorted array):\n "
  print $ insertionSort array
