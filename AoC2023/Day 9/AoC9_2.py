A = open('input9.txt','r')
C = A.read().splitlines()
total = 0

def all_zero(l):
    for i in l:
        if i != 0:
            return False
    return True

def find_dif(l, B):
    if all_zero(l):
        return None
    i = 1
    aux = []
    while i <len(l):
        aux.append(int(l[i])-int(l[i-1]))
        i+=1
    B.append(aux)
    return find_dif(aux, B)

for el in C:
    B = []
    B.append(el.split())
    find_dif(el.split(), B)
    for row in range(len(B)-1, -1, -1):
        if row == len(B)-1:
            B[row].insert(0, 0)
        else:
            B[row].insert(0, int(B[row][0])-int(B[row+1][0]))
    total += B[0][0]
print(total)

