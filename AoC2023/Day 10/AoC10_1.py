D = open('input10.txt').read().strip()
L = D.split('\n')

G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])
cont = 0
pipe = {'|':['n','s'], '7':['w', 's'], 'F':['e', 's'],
        '-':['w','e'], 'J':['n', 'w'], 'L':['n','e']}

def firstmove(G, i, j):
    possible_ways = []
    possible_ways.append((i-1, j, 's')) if ((i-1 >= 0) and (G[i-1][j] in ['|','7','F'])) else print('arriba no')
    possible_ways.append((i, j+1, 'w')) if ((j+1 < C) and (G[i][j+1] in ['-','7','J'])) else print('este no')
    possible_ways.append((i+1, j, 'n')) if ((i+1 < R) and (G[i+1][j] in ['|','L','J'])) else print('sur no')
    possible_ways.append((i, j-1, 'e')) if ((j-1 >= 0) and (G[i][j-1] in ['-','L','F'])) else print('oeste no')
    return possible_ways


def move(G, i, j, cont, prev, pipe):
    cur = G[i][j]
    if cur == 'S':
        total =(cont+1)//2
        print(total)
        return i, j, None, True
    else:
        next = pipe[cur][0] if pipe[cur][0]!= prev else pipe[cur][1]
        G[i][j] = str(cont)
        
        if next == 'n':
            return i-1, j, 's', False
        if next == 'e':
            return i, j+1, 'w', False
        if next == 's':
            return i+1, j, 'n', False
        if next == 'w':
            return i, j-1, 'e', False

    return

for i, l in enumerate(G):
    if 'S' in l:
        for j, c in enumerate(l):
            if c == 'S':
                initial = (i, j)
                break

pw = firstmove(G, initial[0], initial[1])[0]
cont = 1
i, j, prev = pw
final = False

while not final:
    i, j, prev, final = move(G, i, j, cont, prev, pipe)
    cont += 1
