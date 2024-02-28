import random

yes_answer = 0
no_answer = 0

while no_answer <3:
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    correct = num1 + num2
    num = int(input(f"{num1} + {num2}  = "))

    if num == correct:
        print("Правильно!")
        yes_answer = yes_answer + 1
    else:
        print("Ответ неверный")
        no_answer = no_answer + 1

print(f"Игра окончена. Правильных ответов: {yes_answer}")