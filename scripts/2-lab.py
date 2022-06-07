#decomposition

from random import randint
from math import floor, inf

u = int(input("Enter a number of users: "))       #users
m = int(input("Enter a number of movies: "))      #movies

#None array filling
noneList = lambda n: [None for x in range(n)]

D = dict()            #matrix: (film, preferances)

#rating generating
for user in range(1, u + 1):
  movies = [x + 1 for x in range(m)]          #movies ratings for one user
  for index in range(1, m):
    swapRating = movies[index]
    randIndex = randint(0, m - 1)
    movies[index] = movies[randIndex]
    movies[randIndex] = swapRating
  D[user] = movies.copy()

#show matrix
for user in D: print(f"User {user}: {D[user]}")

x = int(input("Enter a user for comprasion: "))         #user for comparison
priorityList = dict()                                   #priority arrays

for user in D:
  if user == x: continue
  userPriorities = noneList(m)
  for i in range(m):
    userPriorities[D[x][i] - 1] = D[user][i]
  priorityList[user] = userPriorities.copy()
# print(priorityList)

#counting inversions function
inv_count = 0
def Inverions_count(arr):
  global inv_count
  if len(arr) == 1: return arr
  n1 = floor(len(arr) / 2)
  n2 = n1
  if len(arr) % 2: n1 += 1
  #dividing into two lists
  left = noneList(n1)
  right = noneList(n2)
  i_1 = i_2 = 0
  while i_1 != len(arr):
    if i_1 < n1:
      left[i_1] = arr[i_1]
    else:
      right[i_2] = arr[i_1]
      i_2 += 1
    i_1 += 1
  #recursive calling
  Inverions_count(left)
  Inverions_count(right)
  l = r = 0
  #adding last element (infitiny number)
  left.append(inf)
  right.append(inf)
  #sorting
  arrLength = len(arr)
  for i in range(arrLength):
    if left[l] <= right[r]:
      arr[i] = left[l]
      l += 1
    else:
      arr[i] = right[r]
      inv_count += (len(right) - l) + 1     #inversions counting for one element
      r += 1
  return arr

priorityInversions = dict()                #priority sequence

for user in priorityList:
  if user == x: continue
  Inverions_count(priorityList[user])
  priorityInversions[user] = inv_count
  inv_count = 0
# print(priorityInversions)

#inversions gradation
inv_arr = list()
for user in priorityInversions:
  inv_arr.append(priorityInversions[user])
inv_arr.sort()
# print(inv_arr)

#output
for inversions in inv_arr:
  for user in priorityInversions:
    if inversions is priorityInversions[user]:
      print(f"User {user}: {inversions} inversions")
      priorityInversions[user] = None
