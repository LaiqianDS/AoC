from collections import defaultdict

a = open('input11.txt', 'r')
C = a.read().splitlines()
L = len(C[0])

rows = []
columns = [i for i in range(L)]
galaxies = []

for i, row in enumerate(C):
    has_galaxy = False    
    for j, c in enumerate(row):
        if c == '#':
            if j in columns:
                columns.remove(j)
            has_galaxy = True
    if not has_galaxy:
        rows.append(i)

dist = defaultdict(list)
for r in range(len(C)):
  for c in range(L):
    if C[r][c]=='#':
      galaxies.append((r,c))

for part2 in [False,True]:
  expansion_factor = 10**6-1 if part2 else 2-1
  ans = 0
  for i,(r,c) in enumerate(galaxies):
    for j in range(i,len(galaxies)):
      r2,c2 = galaxies[j]
      dij = abs(r2-r)+abs(c2-c)
      for er in rows:
        if min(r,r2)<=er<=max(r,r2):
          dij += expansion_factor
      for ec in columns:
        if min(c,c2)<=ec<=max(c,c2):
          dij += expansion_factor
      ans += dij
  print(ans)