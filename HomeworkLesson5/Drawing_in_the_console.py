h = int(input('Please enter height: '))

i = 0
while i < h:
    j = 0
    while j < h * 2:
        if h - 1 - i <= j <= h - 1 + i:
            print('* ', end="")
        else:
            print('  ', end="")
        j += 1
    print()
    i += 1
print()

for i in range(h + 1):
    for j in range(2 * h + 1):
        if (h-j == i) or (j-h == i) or i == h:
            print('* ', end="")
        else:
            print('  ', end="")
    print()





