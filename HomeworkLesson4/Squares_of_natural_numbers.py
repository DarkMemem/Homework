number = int(input("Enter the number to which you want to know all the squares: "))

i = 1
while i ** 2 <= number:
    print(i ** 2, end=" ")
    i += 1
