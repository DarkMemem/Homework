while True:
    number = int(input("Please enter three-digit number: "))

    if 1000 > number > 99:
        tmp_number = str(number)
        tmp_number = int(tmp_number[::-1])
        print(int(tmp_number))
        break
    else:
        print("Repeat please")
