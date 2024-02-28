result = ""
while True:
    a = input("Введите слово, для окончания введите стоп ")
    result = result + a + " "
if a == "стоп":
    print(result)
