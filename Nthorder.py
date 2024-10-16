ans = 1
base = 3
exp = 4
while exp > 0:
    if exp % 2!=0:
        exp -= 1
        ans = ans * base
    else:
        exp //= 2
        base = base * base
print(ans)
