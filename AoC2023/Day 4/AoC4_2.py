import re
from collections import defaultdict

f = open('input4.txt', 'r')
content = f.read().splitlines()
sc = defaultdict(int)

for line in content:
    game, nums = re.split(r':', line)
    game_id = game.strip().split()[1]
    sc[int(game_id)] += 1
    winning, got = nums.split('|')
    w_list = winning.strip().split()
    g_list = got.strip().split()
    cont = 0
    for w in w_list:
        if w in g_list:
            cont += 1
    for i in range(cont):
        sc[int(game_id)+1+i] += 1 * sc[int(game_id)]

total = sum(sc.values())
print(total)
