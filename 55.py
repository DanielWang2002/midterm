n = int(input("請輸入一個正整數(<10):"))
for i in range(1,n+1):
    for k in range(1,i+1):
        print("%2d" %(k*i),end=" ")
    print()