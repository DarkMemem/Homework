#first option
while True:
    number = int(input("Please enter three-digit number: "))

    if 1000 > number > 99:
        tmp_number = str(number)
        tmp_number = int(tmp_number[::-1])
        print("Yor number:", int(tmp_number), sep="")
        break
    else:
        print("Repeat please")

#second option
dir1 = number % 10
dir2 = number // 10 % 10
dir3 = number // 100
print("Yor number:", dir1, dir2, dir3, sep="")

