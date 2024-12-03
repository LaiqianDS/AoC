A = open('input14.txt')
R = A.read().strip().splitlines()
G = [[c for c in r] for r in R]

LR = len(R[0])
LC = len(G)
U = {i:0 for i in range(LR)}

for c in range(LC):
    for _ in range(LR):
        for r in range(LR):
            if G[r][c]=='O' and r>0 and G[r-1][c]=='.':
                G[r][c]='.'
                G[r-1][c] = 'O'

ans = 0
for r in range(LC):
    for c in range(LR):
        if G[r][c] == 'O':
            ans += LC-r

print(ans)