ans = input("請輸入第一組數字:")
s = input("請輸入第二組數字:")
A = 0
B = 0
for i in range(len(s)):
    if (s[i] == ans[i]):
        A += 1
    elif (s[i] in ans):
        B += 1
if A != 4:
    print("%dA%dB 加油" %(A,B))
else:
    print("%dA%dB 全對" %(A,B))