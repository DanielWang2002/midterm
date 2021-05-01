A = input("請輸入A的朋友：").split(" ")
B = input("請輸入B的朋友：").split(" ")
if len(A) > len (B):
    A,B = B,A
c = 0
for i in range(len(A)):
    if A[i] in B:
        c += 1
print("%d" %(c))