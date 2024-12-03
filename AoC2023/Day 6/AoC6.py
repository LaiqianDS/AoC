import re

# Get input
a = open('input6.txt', 'r')
t, d = a.read().splitlines()
tt = t.split(':')[1]
dd = d.split(':')[1]
tl = re.split(r'\W+', tt.strip())
dd = re.split(r'\W+', dd.strip())

# Calculate possible combinations - part 1
total1 = 1
for i, ms in enumerate(tl):
    partial = 0
    partial += sum([(int(ms)-j)*j > int(dd[i]) for j in range(int(ms))])
    total1 *= partial

# Calculate part 2
time = int(''.join(tl))
distance = int(''.join(dd))
total2 = sum([(time-i)*i > distance for i in range(time)]) #O(n)

print(total1)
print(total2)