name = int(input("Введите номер вашего места "))

if name in range(37,54) and name % 2 != 0:
    print("Боковое нижнее")
elif name in range(37, 54) and name % 2 == 0:
    print("Боковое верхнее")
elif name in range(1,36) and name % 2 != 0:
    print("Купе нижнее")
elif name in range(1,36) and name % 2 == 0:
    print("Купе верхнее")
