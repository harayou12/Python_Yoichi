import queue
import math
Year = int(input('何年?>'))
Month = int(input('何月?>'))
Day = int(input('何日?>'))
Zeller = {1: "日曜日", 2: "月曜日", 3: "火曜日", 4: "水曜日", 5: "木曜日", 6: "金曜日", 0: "土曜日"}
if Year % 4 == 0: #4の倍数になる年はうるう年
    FebDay = 29
elif Year % 100 == 0 and Year % 400 != 0: #例外として100の倍数になる年の中で400で割り切れない年は平年
    FebDay = 28
else: 
    FebDay = 28
DayInMonth = {1: 31, 2: FebDay, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} #各月の日数を指定
c = math.floor(Year / 100) #床関数利用
y = Year % 100
p = -2 * c + math.floor(c / 4)
h = (Day + math.floor( 26 / 10 * (Month + 1)) + y + math.floor(y / 4) + p) % 7 #ツェラーの公式利用
print(str(Year)+"年"+str(Month)+"月"+str(Day)+"日は"+str(Zeller[h]))
q = queue.Queue() #FIFO型のキューを定義
print("--------以下, その週の曜日を求める----------")
for i in range(0,7):
    NewDay = i + Day - h
    if 0 < NewDay <= int(DayInMonth[Month]): #月をまたがない場合
        z = Zeller[i]
        q.put(str(Year)+"年"+str(Month)+"月"+str(i+Day-h)+"日は"+str(z))
        i =+ 1
    elif NewDay <= 0: #月初の日が指定されてあり,月をまたぐ場合
        if Month == 1: #1月で年もまたぐ場合の例外処理
            NewMonthMinus = 12
            NewYearMinus = Year - 1
            NewDayMinus = Day + DayInMonth[NewMonthMinus]
        else:
            NewMonthMinus = Month - 1
            NewYearMinus = Year
            NewDayMinus = Day + DayInMonth[NewMonthMinus]
        z = Zeller[i]
        q.put(str(NewYearMinus)+"年"+str(NewMonthMinus)+"月"+str(i+NewDayMinus-h)+"日は"+str(z))
        i =+ 1
    else: #月末の日が指定されてあり,月をまたぐ場合
        if Month == 12: #12月で年もまたぐ場合の例外処理
            NewMonthPlus = 1
            NewYearPlus = Year + 1
        else:
            NewMonthPlus = Month + 1
            NewYearPlus = Year
        z = Zeller[i]
        q.put(str(NewYearPlus)+"年"+str(NewMonthPlus)+"月"+str(i+Day-h-DayInMonth[Month])+"日は"+str(z))
        i =+ 1
while not q.empty():
    print(q.get())
