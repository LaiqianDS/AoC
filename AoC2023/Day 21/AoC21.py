A = open('input.txt')
G = [[c for c in r] for r in A.read().splitlines()]

R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            initial = (r, c)

V = [0, 1, 0, -1]
H = [1, 0, -1, 0]
t = 0
seen = set()
pos = [initial]
cont = 0

def distance(r, c, initial):
        return abs(r-initial[0])+abs(c-initial[1])

while t < 26501365:    
    l = len(pos)
    for p in pos.copy():
        for i in range(4):
            if (0 < p[0]+V[i] < R) and (0 < p[1]+H[i] < C) and (p[0]+V[i], p[1]+H[i]) not in seen and G[p[0]+V[i]][p[1]+H[i]] != '#':
                seen.add((p[0]+V[i], p[1]+H[i]))
                pos.append((p[0]+V[i], p[1]+H[i]))

    pos = pos[l:]
    t += 1
    if len(pos)==0:
        print(t)
        break

for (x, y) in seen:
    if (distance(x, y, initial)%2==1):
        cont += 1

print(cont*202300)
