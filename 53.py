w = float(input("請輸入路程公里數(km):"))
w -= 1.5
m = 0
if w <= 0:
    m = 75
else:
    if w % 0.25 == 0:
        m = 75 + (5*w//0.25)
    else:
        m = 75 + (5*((w//0.25)+1))
print("所需車資為:%d" %(m))