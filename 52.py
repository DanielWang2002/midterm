n = int(input("輸入n值:"))
w = {}
for i in range(n):
    t = input("請輸入姓名:")
    r = input("請輸入電子郵件:")
    w[t] = r
x = input("請輸入要查詢電子郵件的姓名:")
print("%s 電子郵件帳號為 %s" %(x,w[x]))