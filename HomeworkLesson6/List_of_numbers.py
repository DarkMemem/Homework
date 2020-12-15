from random import randint

lst = [randint(10, 50) for _ in range(20)]
print(lst)
n = 0
for i in range(1, len(lst)-1):
    if int(lst[i-1]) < int(lst[i]) and int(lst[i]) > int(lst[i+1]):
        n += 1

print(n)
