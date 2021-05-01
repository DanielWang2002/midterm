w = []
for i in range(10):
    print("請輸入第%d個數字:" %(i+1),end="")
    w.append(int(input()))
w.sort()
print("最大的3個數字為:%d,%d,%d" %(w[9],w[8],w[7]))
print("最小的3個數字為:%d,%d,%d" %(w[2],w[1],w[0]))