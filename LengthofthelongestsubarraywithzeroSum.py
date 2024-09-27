def maxLen(A, n):
    mpp = {}
    maxi = 0
    sum = 0
    for i in range(n):
        sum += A[i]
        if sum == 0:
            maxi = i + 1
        else:
            if sum in mpp:
                print(mpp,maxi)
                maxi = max(maxi, i - mpp[sum])
            else:
                mpp[sum] = i
    return maxi


arr = [9,9,9,0,-9]
maxLen(arr,len(arr))
