s = input().split(",")
m = []
for i in range(len(s)):
    for k in range(i+1,len(s)):
        t1 = int(s[i])
        t2 = int(s[k])
        while(t1 != t2):
            if t1 > t2:
                t1 -= t2
            else:
                t2 -= t1
        m.append(t1)
print("%d" %(max(m)))