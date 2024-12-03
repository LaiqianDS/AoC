from collections import defaultdict
a = open('input7.txt', 'r')
content = a.read().splitlines()
d = defaultdict(list)

def classify(d, h, b):
    aux = {}
    for card in h:
        aux[card] = aux.get(card, 0) + 1
    if sorted(aux.values()) == [5]:
        d['Five of a kind'].append((h,b))
    elif sorted(aux.values()) == [1,4]:
        d['Four of a kind'].append((h,b))
    elif sorted(aux.values()) == [2,3]:
        d['Full house'].append((h,b))
    elif sorted(aux.values()) == [1,1,3]:
        d['Three of a kind'].append((h,b))
    elif sorted(aux.values()) == [1,2,2]:
        d['Two pair'].append((h,b))
    elif sorted(aux.values()) == [1,1,1,2]:
        d['One pair'].append((h,b))
    elif sorted(aux.values()) == [1,1,1,1,1]:
        d['High card'].append((h,b))

for i in range(len(content)):
    hand, bid = content[i].split()
    classify(d, hand, bid)

aux = []
aux2 = ['High card', 'One pair', 'Two pair','Three of a kind', 'Full house', 'Four of a kind', 'Five of a kind']
for pack in aux2:
    temp2 = []
    for (h, b) in d[pack]:
        temp = [c for c in h]
        for i, c in enumerate(temp):
            if c == 'A':
                temp[i] = 14
            elif c == 'K':
                temp[i] = 13
            elif c == 'Q':
                temp[i] = 12
            elif c == 'J':
                temp[i] = 11
            elif c == 'T':
                temp[i] = 10
            else:
                temp[i] = int(temp[i])
        temp2.append((temp, b))
    temp2 = sorted(temp2)
    for h, b in temp2:
        aux.append((h,b))

ans = 0
for i,(h,b) in enumerate(aux):
    #print(i,h,b)
    ans += (i+1)*int(b)
print(ans)


def classify2(d, h, b):
    aux = {}
    for card in h:
        aux[card] = aux.get(card, 0) + 1
    if sorted(aux.values()) == [5]:
        d['Five of a kind'].append((h,b))
    elif sorted(aux.values()) == [1,4]:
        if aux.get('J', 0) == 1:
            d['Five of a kind'].append((h,b))
        elif aux.get('J', 0) == 4:
            d['Five of a kind'].append((h,b))
        else:
            d['Four of a kind'].append((h,b))
    elif sorted(aux.values()) == [2,3]:
        if aux.get('J', 0) == 2:
            d['Five of a kind'].append((h,b))
        elif aux.get('J', 0) == 3:
            d['Five of a kind'].append((h,b))
        else: d['Full house'].append((h,b))
    elif sorted(aux.values()) == [1,1,3]:
        if aux.get('J', 0) == 1:
            d['Four of a kind'].append((h,b))
        elif aux.get('J', 0) == 3:
            d['Four of a kind'].append((h,b))
        else: d['Three of a kind'].append((h,b))
    elif sorted(aux.values()) == [1,2,2]:
        if aux.get('J', 0) == 1:
            d['Full house'].append((h,b))
        elif aux.get('J', 0) == 2:
            d['Four of a kind'].append((h,b))
        else: d['Two pair'].append((h,b))
    elif sorted(aux.values()) == [1,1,1,2]:
        if aux.get('J', 0) == 1:
            d['Three of a kind'].append((h,b))
        elif aux.get('J', 0) == 2:
            d['Three of a kind'].append((h, b))
        else: d['One pair'].append((h,b))
    elif sorted(aux.values()) == [1,1,1,1,1]:
        if aux.get('J', 0) == 1:
            d['One pair'].append((h,b))
        else: d['High card'].append((h,b))

d = defaultdict(list)
for i in range(len(content)):
    hand, bid = content[i].split()
    classify2(d, hand, bid)


aux = []
aux2 = ['High card', 'One pair', 'Two pair','Three of a kind', 'Full house', 'Four of a kind', 'Five of a kind']
for pack in aux2:
    temp2 = []
    for (h, b) in d[pack]:
        temp = [c for c in h]
        for i, c in enumerate(temp):
            if c == 'A':
                temp[i] = 14
            elif c == 'K':
                temp[i] = 13
            elif c == 'Q':
                temp[i] = 12
            elif c == 'J':
                temp[i] = 1
            elif c == 'T':
                temp[i] = 10
            else:
                temp[i] = int(temp[i])
        temp2.append((temp, b))
    temp2 = sorted(temp2)
    for h, b in temp2:
        aux.append((h,b))

ans = 0
for i,(h,b) in enumerate(aux):
    #print(i,h,b)
    ans += (i+1)*int(b)
print(ans)