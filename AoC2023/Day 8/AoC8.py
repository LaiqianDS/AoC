A = open('input8.txt', 'r')
C = A.read().splitlines()
instructions = C[0]
B = len(instructions.strip())

mapa = {'L': {}, 'R': {}}
for line in C[2:]:
    node, dest = line.split('=')
    l, r = dest[2:-1].split(', ')
    mapa['L'][node.strip()] = l.strip()
    mapa['R'][node.strip()] = r.strip()

pos = 'AAA'
cont = 0
i = 0

while True:
    if instructions[i] == 'R':
        pos = mapa['R'][pos]
    else: 
        pos = mapa['L'][pos]
    if pos == 'ZZZ':
        break
    i = (i+1) % B
    cont += 1

print(cont+1)
