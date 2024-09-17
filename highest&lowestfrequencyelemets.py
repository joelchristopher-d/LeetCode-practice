arr = [10,5,10,15,10,5]
d={}
n=len(arr)
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
maxval,minval = 0,n
maxele = minele = 0
for i in d:
    if d[i]>maxval:
        maxval = d[i]
        maxele = i
    if d[i]<minval:
        minval = d[i]
        minele = i
print(maxele,minele)
