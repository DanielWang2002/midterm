m = [72,62,82,44,60]
w1 = [55,68]
w2 = ["A","B"]
q = input("請選擇主餐及升級的套餐:")
r = input("是否升級成大杯飲料:")
t = input("是否換成大薯:")
money = m[int(q[0])-1] + w1[w2.index(q[1])]
if r == "是":
    money += 7
if t == "是":
    money += 13
print("總共為:%d元" %(money))