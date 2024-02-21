name = input("Введите год ")

if int(name) % 4 == 0 and int(name) % 100 != 0 :
    print("Год ", name, " - високосный")
else:
    print("Год ", name, " - не високосный")