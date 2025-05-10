a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Оберіть дію (+, -, *, /): ")

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == '/':
    if b == 0:
        print("Ділення на нуль неможливе")
    else:
        print(a / b)
else:
    print("Невідома дія")