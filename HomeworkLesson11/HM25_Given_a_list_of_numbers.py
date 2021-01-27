from random import randint

lst = [randint(10, 50) for _ in range(20)]
print(lst)
k = int(input())
for i in range(k + 1, len(lst)):
    lst[i - 1] = lst[i]
lst.pop()
print(' '.join([str(i) for i in lst]))
