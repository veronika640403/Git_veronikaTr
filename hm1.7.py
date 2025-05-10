rating = int(input("Введіть кількість балів: "))

if 0 <= rating <= 49:
    print("Незадовільно")
elif 50 <= rating <= 69:
    print("Задовільно")
elif 70 <= rating <= 89:
    print("Добре")
elif 90 <= rating <= 100:
    print("Відмінно")
else:
    print("Некоректна кількість балів")