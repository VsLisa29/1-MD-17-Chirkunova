def task_1():
    my_numbers = [1,10,2,3,45]
    number = int(input("Введите число "))

    if number in my_numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")

def task_2():
    list = ["fruit", "milk", "cow", "apple", "milk", "2", "2"]
    repeat_list = []

    for item in list:
        if list.count(item) > 1 and item not in repeat_list:
            repeat_list.append(item)

    if len(repeat_list)>0:
        print(f"Повторяющиеся элементы: {repeat_list}")
    else:
        print("Повторяющихся элементов нет")

def task_3():
    days_of_week = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")

    choose_days = int(input("Сколько выходных вы хотите на неделе? "))

    weekends = days_of_week[-choose_days:]
    work_days = days_of_week[:-choose_days]

    print(f"Ваши выходные дни: {weekends}")
    print(f"Ваши рабочие дни: {work_days}")

def task_4():
    my_group = ['Иванов', 'Кличко', 'Рогозина', 'Селиванов', 'Мурин', 'Кулаков', 'Зарубин', 'Комаров', 'Лазарев']
    other_group = ['Казанова', 'Шелепов', 'Смирнова', 'Ковалев', 'Иванов', 'Спиридонов', 'Парусов', 'Шальнов', 'Курутова', 'Солнечная', 'Губина']

    sport_team = tuple(my_group[:6] + other_group[6:])
    print(f"Моя группа{my_group}")
    print(f"Другая группа{other_group}")
    print(f"Спортивна команда {sport_team}")
    print(f"Длина кортежа {len(sport_team)}")

    sorts_team = sorted(sport_team)
    print(f"Отсортированная список команды: {sorts_team}")

    famil = sport_team.count('Иванов')
    if famil > 0:
        print(f"Фамилия Иванов встречается {famil} раз")
    else:
        print("Иванов не входит в команду")