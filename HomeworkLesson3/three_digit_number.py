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

dig1 = number % 10
dig2 = number // 10 % 10
dig3 = number // 100
print("Yor number:", dig1 * 100 + dig2 * 10 + dig3, sep="")

