input_first = input()
for k in range(2):
    p = input_first.rstrip().split(' ')
n = p[0]
x = p[1]
a=[]
for wi in range(int(n)):
    input_a = input()
    a.append(input_a.rstrip().split(' '))
price=[]
for i in range(int(n)):
    price.append(int(a[i][1])+(1+(int(x)-int(a[i][0]))//int(a[i][2]))*int(a[i][3]))
print(str(min(price))+" "+str(max(price)))
