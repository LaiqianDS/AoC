A = open('input15.txt')
S = A.read().strip().splitlines()
s = ''.join(S)
SS = s.split(',')

def get_hash(string):
    val = 0
    code = ''
    number = ''

    if isinstance(string, int):
        return None
    for i in range(len(str(string))):
        if str(string[i]).isalpha():
            code += string[i]
            val += ord(string[i])
            val *= 17
            val %= 256
        elif string[i].isdigit():
            number += string[i]
        else:    
            operation = string[i]
    return val, code, number, operation

dic = {}
for value in SS:
    if get_hash(value) is not None:
        val, code, number, operation = get_hash(value)
        if operation == '=':
            if val not in dic:
                dic[val] = [(code, number)]
            else:
                appear = False
                pos = 0
                for p, (c, n) in enumerate(dic[val]):
                    if c == code:
                        appear = True
                        pos = p
                        break
                if not appear:
                    dic[val].append([code, number])
                else:
                    dic[val][pos] = (code, number)
        else:
            if not val in dic:
                continue
            else:
                for p, (c, n) in enumerate(dic[val]):
                    if c == code:
                        del dic[val][p]
    
for k, v in dic.copy().items():
    if len(v) == 0:
        del dic[k]

sum = 0
for k, v in dic.items():
    box = k+1
    for p, (c, n) in enumerate(v):
        sum += box*(int(p)+1)*int(n)

print(sum)