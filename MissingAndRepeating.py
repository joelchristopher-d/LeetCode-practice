a = [3,1,2,5,4,6,7,5]
a = [3,1,2,5,3]
a.sort()
print(a)
prev = a[0]
nxt = 0
res = [0,len(a)]
for i in range(1,len(a)):
    prev = a[i-1]
    print(i)
    nxt = a[i]
    if prev == nxt:
        res[0]=prev
    if i not in a:
        res[1]=i
print(res)
