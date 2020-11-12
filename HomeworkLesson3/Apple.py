children = int(input("Please enter the number of children: "))
apple = int(input("Please enter the number of apple: "))

quantity = apple // children
remainder = apple % quantity

print("Each child will receive " + str(quantity) + " apples, and " + str(remainder) + " apples will remain in the basket")
