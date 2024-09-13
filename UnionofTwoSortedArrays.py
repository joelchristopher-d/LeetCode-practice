arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]
i = j = 0
final = []
while i < len(arr1) and j < len(arr2):
    if arr1[i]<=arr2[j]:
        if arr1[i] not in final:
            final.append(arr1[i])
        i+=1
    elif arr1[i]>arr2[j]:
        if arr2[j] not in final:
            final.append(arr2[i])
        j+=1
while i<len(arr1):
    if arr1[i] not in final:
        final.append(arr1[i])
    i+=1
while j<len(arr2):
    if arr2[j] not in final:
        final.append(arr2[j])
    j+=1
print(final)   
