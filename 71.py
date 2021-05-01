n = int(input("請輸入十位數的正整數:"))
ans = ""
while(n):
    ans += str(n % 3)
    n //= 3
print("%d的三進位為%s" %(n,ans[::-1]))