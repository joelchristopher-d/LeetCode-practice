arr = [2, 3, 5, 1, 9]
k = 10
n = len(arr) 
mpp ={}
preSum = 0
maxlen = 0
for i in range(n):
    preSum += arr[i]
    if preSum == k:maxlen=max(maxlen,i+1)
    remove = preSum - k
    if remove in mpp:
        maxlen = max(maxlen,i-mpp[remove])
    if preSum not in mpp:mpp[preSum]=i
print(maxlen)
