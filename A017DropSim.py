input_first = input()
for k in range(3):
    p = input_first.rstrip().split(' ')
h = p[0]
w = p[1]
n = p[2]
hi=[]
for wi in range(int(n)):
    input_h = input()
    hi.append(input_h.rstrip().split(' '))
print(hi)
a=[]
for i in range(int(h)):
    a.append(str(int(w)*"・"))
print(a)
for j in range(0,int(h)-1):
    if a[j][(int(hi[j][2])+1):(int(hi[j][2])+int(hi[j][1]))]==int(hi[j][1])*"・":
        j += 1
    else:
        a[j][int(hi[j-1][2])+1:(int(hi[j-1][2])+int(hi[j-1][1]))]=str(int(hi[j][1])*"#")
print(a)
