import heapq
from collections import defaultdict

def shortestPath(graph, src, dest):
  h = []
  # keep a trach record of vertices with cost
  # heappop will return vertex with least cost
  # greedy Src -> MIN ->MIN ->MIN ->dest
  
  heapq.heappush(h, (0, src))
  print(h)
  path =[]
  while len(h) != 0:
    currcost, currvtx = heapq.heappop(h)
    print("currcost: {}, and currvtx: {}".format(currcost, currvtx))
    if currvtx == dest:
      print("path exists {} to {} with cost {}".format(src, dest, currcost))
      break
    for neigh, neighcost in graph[currvtx]:
      heapq.heappush(h, (currcost + neighcost, neigh))
      print("h: ", h)


graph = defaultdict(list)

v, e = map(int, input().split())
print("v(unique points) = {} and e(number of entries) = {}".format(v,e))

for i in range(e):
  u, v, w = map(str, input().split())
  graph[u].append((v, int(w)))
src, dest = map(str, input().split())
shortestPath(graph, src, dest)


