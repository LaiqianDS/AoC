import heapq

A = open('input.txt').read().strip().splitlines()
G = [[int(c) for c in r] for r in A]

R = len(G)
C = len(G[0])

s = (0, 0)
final = (C - 1, R - 1)

dirs = {">": (1, 0), "v": (0, 1), "^": (0, -1), "<": (-1, 0)}
opposite = {"<": ">", ">": "<", "v": "^", "^": "v"}
to_visit = [(0, ">", s), (0, "v", s)] #two possible initial movements

seen = set()
done = False

while to_visit and not done:
    cost, dir, coords = heapq.heappop(to_visit)
    if (coords, dir) in seen:
        continue
    seen.add((coords, dir))
    for d in dirs:
        n_p = (coords[0] + dirs[d][0], coords[1] + dirs[d][1])
        if (
            not 0 <= n_p[0] < C # out of G range
            or not 0 <= n_p[1] < R
            or (d == dir[-1] and len(dir) == 10) # path longer than 10 blocks
            or (d != dir[-1] and len(dir) < 4) # path shorter than 4 blocks
            or dir[-1] == opposite[d] # turning back
        ):
            continue
        if d == dir[-1]:
            nd = dir + d
        else:
            nd = d
        if (n_p, nd) in seen:
            continue
        if n_p == final:
            print(cost + G[n_p[1]][n_p[0]])
            done = True
            break
        heapq.heappush(to_visit, (cost + G[n_p[1]][n_p[0]], nd, n_p))