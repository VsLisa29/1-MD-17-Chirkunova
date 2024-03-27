def proverka_del():
    number = int(input("Введите число "))
    if number % 7 == 0:
        print(f"{number} делится на 7")
    else:
        print(f"{number} не делится на 7")

def del_200():
    try:
        user_input = input("Введите число для деления 200 ")
        number = float(user_input)
        result = 200 / number
        print(f"Результат деления 200 на {number}: {result}")
    except ValueError:
        print("Ошибка: Введено не число. Пожалуйста, введите число.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль. Пожалуйста, введите число отличное от нуля.")

def magic_date():
    user_date = input("Введите дату в формате ДД.ММ.ГГГГ ")
    day, month, year = map(int, user_date.split('.') )

    if day * month == year % 100:
        print(f"{user_date} Дата является магической")
    else:
        print(f"{user_date} Это обычная дата")

def lucky_ticket():
    ticket_number = input("Введите номер билета: ")

    if len(ticket_number) % 2 != 0:
        return False

    part_len = int(len(ticket_number) / 2)
    first_part = ticket_number[:part_len]
    second_part = ticket_number[part_len:]
    print(f"1: {first_part}")
    print(f"2: {second_part}")

    sum_first_part = sum(map(int, first_part))
    sum_second_part = sum(map(int, second_part))
    print(f"1: {sum_first_part}")
    print(f"2: {sum_second_part}")

    if sum_first_part == sum_second_part:
        print("Этот билет счастливый!")
    else:
        print("Этот билет не счастливый.")