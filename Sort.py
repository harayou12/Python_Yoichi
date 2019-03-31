import random
s = []
n = int(input('幾つのソート?>'))
for i in range(0,n):
    a = random.randint(1, 100)
    print(a)
    s.append(a)
print('ソート前の乱数',s)
for p in range(0,n-1):
    for q in range(p+1,n):
        if s[p] > s[q]:
            z = s[p]
            s[p] = s[q]
            s[q] = z
        else:
            pass
print('ソート後の乱数',s)
print('a')
