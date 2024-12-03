from collections import defaultdict
import networkx as nx

A = open('input.txt')
C = A.read().splitlines()

E = defaultdict(set)
for line in C:
  s,e = line.split(':')
  for y in e.split():
    E[s].add(y)
    E[y].add(s)

G = nx.DiGraph()
for k,vs in E.items():
  for v in vs:
    G.add_edge(k,v,capacity=1.0)
    G.add_edge(v,k,capacity=1.0)

for x in [list(E.keys())[0]]:
  for y in E.keys():
    if x!=y:
      cut_value, (L,R) = nx.minimum_cut(G, x, y)
      if cut_value == 3:
        print(len(L)*len(R))
        break