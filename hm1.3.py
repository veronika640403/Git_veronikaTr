import random

number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Вгадай число від 1 до 10: "))
    if guess == number:
        print("Вгадано")
        break
    elif guess < number:
        print("Більше")
    else:
        print("Менше")
    attempts -= 1

if attempts == 0:
    print(f"На жаль, ти не вгадав. Число було: {number}")