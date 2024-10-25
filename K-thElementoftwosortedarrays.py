
def kthElement(a, b, m, n, k):
    ele = -1
    cnt = 0
    i, j = 0, 0
    while i < m and j < n:
        if a[i] < b[j]:
            if cnt == k - 1:
                ele = a[i]
                print(ele)
            cnt += 1
            i += 1
        else:
            if cnt == k - 1:
                ele = b[j]
                print(ele)
            cnt += 1
            j += 1

    while i < m:
        if cnt == k - 1:
            ele = a[i]
            print(ele)
        cnt += 1
        i += 1
    while j < n:
        if cnt == k - 1:
            ele = b[j]
            print(ele)
        cnt += 1
        j += 1
    return ele
            
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
kthElement(a,b,len(a),len(b),5)
        
