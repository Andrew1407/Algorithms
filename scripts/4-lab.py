#Pyramid (medians)

A = [30, 19, 9, 15, 55, 24, 3, 78, 46, 41]
A_length = len(A)
print(f"Original array: {A}\n\nPyramid:\n")
a = list()          #increasing array
i = 0
u = len(A) - 1
medians = dict()    #key: number of itetarions, value: medians
arrays = list()     #list of obtained arrays
t = ''              #space distance
tt = list()         #spacing list
for s in range(A_length):
  tt.append(t)
  t += ' '

#pyramid output, medians searching
while u >= 0:
  a.append(A[i])                    #array filling
  arrays.append(a.copy())
  #medians finding
  if (len(a) % 2):                  #if length is odd
    mid = a[int(len(a) / 2)]
    medians[i + 1] = mid
  else:                             #if it's even one
    mid = a[int((len(a) / 2) - 1)], a[int(len(a) / 2)]
  medians[i + 1] = mid
  #pyramid output(iterations's left to)
  print(f"{i + 1}\t{tt[u]} {a}\n")
  i += 1
  u -= 1

#medians output
print("\n\nMedians:\n")
for i in range(len(arrays)):
  print(f"Array:{arrays[i]}\nNumber of iterations (process time): {i + 1}")
  print(f"Median(s): {medians[i + 1]}\n")
