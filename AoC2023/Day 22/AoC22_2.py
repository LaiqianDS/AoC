from collections import deque

A = open('Day 22/input.txt')
C = A.read().strip().split('\n')
B = [list(map(int, r.replace("~", ",").split(","))) for r in C]

B.sort(key=lambda brick: brick[2])

def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

for index, brick in enumerate(B):
    max_z = 1
    for check in B[:index]:
        if overlaps(brick, check):
            max_z = max(max_z, check[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z
    
B.sort(key=lambda brick: brick[2])

k_supports_v = {i: set() for i in range(len(B))}
v_supports_k = {i: set() for i in range(len(B))}

for j, upper in enumerate(B):
    for i, lower in enumerate(B[:j]):
        if overlaps(lower, upper) and upper[2] == lower[5] + 1:
            k_supports_v[i].add(j)
            v_supports_k[j].add(i)

total = 0

for i in range(len(B)):
    q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
    falling = set(q)
    falling.add(i)
    
    while q:
        j = q.popleft()
        for k in k_supports_v[j] - falling:
            if v_supports_k[k] <= falling:
                q.append(k)
                falling.add(k)
    
    total += len(falling) - 1

print(total)