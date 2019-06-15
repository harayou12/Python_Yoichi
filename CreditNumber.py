input_line = int(input())
t = []
for i in range(0,input_line):
    t.append(str(input()))
even = 0
odd = 0
for q in range(0,input_line):
    for j in range(0,7):
        temp_even = 2 * int(t[q][2*j]) #[]が奇数
        if temp_even > 9:
            let_even = str(temp_even)
            even_sum = int(let_even[0]) + int(let_even[1])
        else:
            even_sum = 2 * int(t[q][2*j])
        even += even_sum
        odd += int(t[q][2*j+1]) #[]が偶数
    sum_eo = even+odd
    temp_sum=str(sum_eo)
    if int(temp_sum[1]) == 0:
        x = 0
        print(0)
    else:
        x = 10 - int(temp_sum[1])
        print(x)
