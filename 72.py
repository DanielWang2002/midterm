n = int(input("請輸入n:"))
k = int(input("請輸入k:"))
g = int(n)
while(g):
    g //= k
    n += g