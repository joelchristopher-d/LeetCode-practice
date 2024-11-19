#  Form a number system with only 3 and 4. Find the nth number of the number system. 
# Eg.) The numbers are: 3, 4, 33, 34, 43, 44, 333, 334, 343, 344, 433, 434, 443, 444, 3333, 3334, 3343, 3344, 3433, 3434, 3443, 3444 ….



num1 = 3
num2 = 4
queue = ["3","4"]
k = 100
# print(queue.pop(0))
result = ["3","4"]
temp = ""
for i in range(k):
    temp = queue.pop(0)
    queue.append(temp+"3")
    queue.append(temp+"4")
print(temp)
