result = ""
while True:
    a = input("Введите слово, для окончания введите стоп ")
    if a == "стоп":
        print(result)
        break
    else:
        result = result + a + " "
