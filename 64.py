def isPrime(num):
    c = True
    for i in range(num-1,1,-1):
        if num % i == 0:
            c = False
            break
    if c == True:
        return True
    else:
        return False
q = int(input("請輸入第一個要判斷的數字："))
w = int(input("請輸入第二個要判斷的數字："))
if (isPrime(q)) & (isPrime(w)) & ((q-w==2) | (w-q==2)):
    print("Y")
else:
    print("N")