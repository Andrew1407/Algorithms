# insertion sort

A = [30, 19, 9, 15, 55, 24, 3, 78, 46, 41]
print(f"Input array:\n {A}\n\n")
index = 0

#main iteration
while index != (len(A) - 1):
  index += 1              #iterable index
  value = A[index]        #an array value of the index
  
  #for odd numbers
  if A[index] % 2:
    i = index - 1
    while A[i] % 2:                  #if value <= A[i]
      if A[index] <= A[i]:            #position searching
        A.insert(i + 1, A[index])
        A.pop(index + 1)
        break
      i -= 1
    if not A[i] % 2:                  #if value is maximum
      A.insert(i + 1, A[index])
      A.pop(index + 1)
      
  #for even numbers
  else:
    if A[0] % 2:                 #if the first item is odd
      A.insert(0, A[index])
      A.pop(index + 1)
      #output after iteration
      print(f"{A}, iteration: {index}; placed value: {value};\n")
      continue
    i = 0
    while not A[i] % 2:           #if A[index] <= A[i]
      if A[index] <= A[i]:        #position searching
        A.insert(i, A[index])
        A.pop(index + 1)
        break
      i += 1
    if A[i] % 2:                  #if value is maximum
      A.insert(i, A[index])
      A.pop(index + 1)
      
  #output after iteration
  print(f"{A}, iteration: {index}; placed value: {value};\n")

#final result output
print('Sorted array:\n ', A)
