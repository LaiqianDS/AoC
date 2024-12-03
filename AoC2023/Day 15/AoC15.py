A = open('input15.txt')
S = A.read().strip().splitlines()
s = ''.join(S)
SS = s.split(',')

def get_hash(string):
    val = 0
    for i in range(len(string)):
        val += ord(string[i])
        val *= 17
        val %= 256
    return val

values = [get_hash(s) for s in SS]
print(sum(values))