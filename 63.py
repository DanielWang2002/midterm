n = int(input("請輸入正整數n:"))
ar = []
for i in range(n-1,0,-1):
    if n % i == 0:
        ar.append(i)
if n == sum(ar):
    print("perfect")
elif sum(ar) < n:
    print("deficient")
else:
    print("abundant")