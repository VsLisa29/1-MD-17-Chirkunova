while True:
    a = input("Введите слово ")
    if "ф" in a:
        print("Ого! Это редкое слово!")
    elif a == "стоп":
        break
    else:
        print("Эх, это не очень редкое слово...")
