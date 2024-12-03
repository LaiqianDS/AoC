file = 'input5.txt'
a = open(file, 'r')
parts = a.read().strip().split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]
lines = []
lines_tuples = []
for s in others:
    lines.append(s.split('\n')[1:])
for line in lines:
    temp = []
    for el in line:
        temp.append(tuple(el.split(' ')))
    lines_tuples.append(temp)

def apply_one(s, t):
    for change in t:
        for dst, src, rg in change:
            if int(src) <= s < int(src)+int(rg):
                s = int(dst) + int(s) - int(src)
                break
    return s

seeds_loc = []
for s in seed:
    seeds_loc.append(apply_one(s, lines_tuples))

print('part 1:' + str(min(seeds_loc)))