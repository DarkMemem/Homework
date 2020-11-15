number = int(input("Please enter three-digit number: "))

dig1 = number % 10
dig2 = number // 10 % 10
dig3 = number // 100
print("Your number:", dig1 * 100 + dig2 * 10 + dig3, sep="")
