def arithmetic(x, y, z):
    if z == "+":
        return (x + y)
    elif z == "-":
        return (x - y)
    elif z == "*":
        return (x * y)
    elif z == "/":
        return (x / y)
    else:
        return ("Invalid operation")


x = int(input('Введите первое число : '))
y = int(input('Введите второе чиcло : '))
z = input('Введите знак (+, - , * , /) : ')
print(arithmetic(x, y, z))
