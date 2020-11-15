class1 = int(input("Enter the number of students in the first class: "))
class2 = int(input("Enter the number of students in the second class: "))
class3 = int(input("Enter the number of students in the third class: "))

Desk_in_first_class = class1 / 2
Desk_in_second_class = class2 / 2
Desk_in_third_class = class3 / 2

if Desk_in_first_class % 1 == 0.5:
    Desk_in_first_class += 1

if Desk_in_second_class % 1 == 0.5:
    Desk_in_second_class += 1

if Desk_in_third_class % 1 == 0.5:
    Desk_in_third_class += 1

print("First class requires ", int(Desk_in_first_class), " desk")
print("Second class requires ", int(Desk_in_second_class), " desk")
print("Third class requires ", int(Desk_in_third_class), " desk")

