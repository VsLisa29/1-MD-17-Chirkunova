def task_1():
    import json

    with open("file10.json", encoding="UTF-8") as file_in:
        file_read = json.load(file_in)

    for product in file_read['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])

        if product['available']:
            print("В наличии\n")
        else:
            print("Нет в наличии!\n")


def task_2():
    import json

    with open("file10.json", encoding="UTF-8") as file_in:
        file_read = json.load(file_in)

    user_product = {'name': input("Введите названия продукта "),
                    'price': int(input("Введите цену продукта ")),
                    'weight': int(input("Введите вес продукта ")),
                    'available': input("В наличии? (Да/Нет) ")
                    }

    if user_product['available'] == "Да":
        user_product['available'] = True
    elif user_product['available'] == "Нет":
        user_product['available'] = False
    else:
        print("Введите только Да или Нет ")

    file_read['products'].append(user_product)

    with open("file10.json", "w") as file_in:
        json.dump(file_read, file_in)

    for product in file_read['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])

        if product['available']:
            print("В наличии\n")
        else:
            print("Нет в наличии!\n")


def task_3():
    en_ru_dictionary = {}

    with open("en-ru.txt", encoding="UTF-8") as file:
        for line in file:
            key, value = line.strip("\n").split('-')
            en_ru_dictionary[key] = value

    print(en_ru_dictionary)

    ru_en_dictionary = {
        value: key
        for key, value
        in en_ru_dictionary.items()
    }

    sorted_ru_en_dictionary = dict(sorted(ru_en_dictionary.items()))

    print(sorted_ru_en_dictionary)

    with open('ru-en.txt', 'w', encoding="UTF-8") as convert_file:
        for key, value in sorted_ru_en_dictionary.items():
            convert_file.write(f'{key} - {value}\n')