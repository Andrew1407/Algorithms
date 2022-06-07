#greedy alhorithms («Travelling salesman problem»)

from random import randint
from math import inf

#[Graph initialization]
class Graph:
  def __init__(self, num):
    E = self.edges = dict()
    V = self.vertices = range(1, num + 1)
    #edges generating
    for i in V:
      for u in range(i, num + 1):
        if i is u: continue
        key = f"{i} | {u}"
        E[key] = randint(5,30)
    # print(E)

  #searching the shortest way through
  def short_way(self):
    print("[Searching the shortest way]:")
    E = self.edges
    V = list(self.vertices)
    w = self.ways = [V.copy()]
    v = V.copy()
    #generating inversions(ways)
    for i in range(len(V)):
      for u in range(i + 1, len(V)):
        p = v[i]
        v[i] = v[u]
        v[u] = p
        w.append(v)
        v = V.copy()
    V.reverse()
    w.append(V.copy())
    v = V.copy()
    for i in range(len(V)):
      for u in range(i + 1, len(V)):
        p = v[i]
        v[i] = v[u]
        v[u] = p
        if v in w: continue
        w.append(v)
        v = V.copy()
    #weight ways
    ways = dict()
    for arr in w:
      i, sum  = 0, 0
      while i < (len(arr) - 1):
        a = arr[i]
        b  =arr[i + 1]
        key = f"{a} | {b}" if a < b else f"{b} | {a}"
        sum += E[key]
        i += 1
      ways[str(arr)] = sum
    # print(ways)
    #get minimun path value
    min_way = inf
    key = None
    for i in ways:
      if ways[i] < min_way:
        min_way = ways[i]
        key = i
    print(f"The shortest way is {min_way} through {key}.")
    return min_way

#[Graph usage]
graph1 = Graph(5)
print("[Graph_1]:")
print(f"vertices: 5\nedges:\n{graph1.edges}")
graph1.short_way()

graph2 = Graph(7)
print("\n[Graph_2]:")
print(f"vertices: 7\nedges:\n{graph2.edges}")
graph2.short_way()
