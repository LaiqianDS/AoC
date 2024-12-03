import math
from itertools import cycle

A = open('input8.txt', 'r')
C = A.read().splitlines()
instructions = C[0]
B = len(instructions.strip())

mapa = {}
for line in C[2:]:
    node, dest = line.split('=')
    l, r = dest[2:-1].split(', ')
    mapa[node.strip()] = (l.strip(),r.strip())

def path(start):
    r = 0
    cur = start
    for action in cycle(instructions):
        if cur.endswith("Z"):
            break

        r += 1
        cur = mapa[cur][action == "R"]
    return r

got = [path(start) for start in mapa if start.endswith("A")]
print(math.lcm(*got))
