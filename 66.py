a = input("請輸入string_a：")
b = input("請輸入string_b：")
if len(a) > len(b):
    a,b = b,a
c = []
for i in range(len(a)):
    if (a[i] in b) & (not(a[i] in c)):
        c.append(a[i])
c.sort()
ans = ""
for i in c:
    ans += i
if len(ans) > 0:
    print(ans)
else:
    print("N")