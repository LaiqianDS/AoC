import re

f = open('input4.txt', 'r')
content = f.read().splitlines()
total = 0

for line in content:
    game, nums = re.split(r':', line)
    winning, got = nums.split('|')
    w_list = winning.strip().split()
    g_list = got.strip().split()
    cont = 0
    for w in w_list:
        if w in g_list:
            cont += 1
    sum = 1
    for i in range(cont):
        sum *= 2
    sum //= 2
    total += sum
print(total)
