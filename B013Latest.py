input_first = input()
for i in range(3):
    p = input_first.rstrip().split(' ')
a = p[0] #配座駅へまで時間 a 分
b = p[1] #配座駅から儀野駅の乗車時間 b 分
c = p[2] #儀野駅から会社までの時間 c 分
n=input() #配座駅から出る電車の本数を表す整数 N
hm=[]
for wi in range(int(n)):
    input_hm = input()
    hm.append(input_hm.rstrip().split(' '))
arrival_time=[]
dep_time=[]
for j in range(int(n)):
    arrival_time.append(int(hm[j][0])*60+int(hm[j][1])+int(b)+int(c))
    dep_time.append(int(hm[j][0])*60+int(hm[j][1])-int(a))
    if arrival_time[j] >= 540:
        if int(dep_time[j-1])%60 >= 10:
            print('0'+str(dep_time[j-1]//60)+':'+str(dep_time[j-1]%60))
        else:
            print('0'+str(dep_time[j-1]//60)+':0'+str(dep_time[j-1]%60))
        exit
    else:
        if j == int(n)-1:
            if dep_time[j]%60 >= 10:
                print('0'+str(dep_time[j]//60)+':'+str(dep_time[j-1]%60))
            else:
                print('0'+str(dep_time[j]//60)+':0'+str(dep_time[j]%60))
        else:
            pass
