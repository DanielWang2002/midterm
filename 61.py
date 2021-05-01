q = input("請輸入遊戲時間：").split(":")
t = (int(q[0])*60 + int(q[1]) - 75) // 30
cs = 0
for i in range(1,t+1):
    if i % 3 == 0:
        cs += 7
    else:
        cs += 6
    if i % 2 == 0:
        cs -= 1
print("%d隻兵" %(cs))