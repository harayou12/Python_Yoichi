import csv
import random
import numpy as np
a = []
with open('Member.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばしたい時
    i = 1
    for row in reader:
        a.append(row)
Group_Number = len(a) // 2
for i in range(0, len(a)):
    print(str(a[i]) + 'さんは' + str(random.randint(1,Group_Number)) + '日目発表です')
