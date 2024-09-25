# brute:

array = [5,4,3,2,1]
array = [5,3,2,1,4]
array = [1,2,3,4,5]
pair = 0
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            pair+=1
print(pair)
