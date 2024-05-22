from tkinter import *
def task_1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"{self.restaurant_name} открыт")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def list_flavors(self):
            print(f"Список сортов мороженого в '{self.restaurant_name}' :")
            for flavor in self.flavors:
                print(f" - {flavor}")
            print("\n")

    IceCreamStand1 = IceCreamStand("Золотая рыбка", "Кафе-мороженое", ["фисташковое", "пломбир", "шоколадное", "крем-брюле", "клубничное"])
    IceCreamStand2 = IceCreamStand("Сокровищница", "Кафе-мороженое", ["пломбир", "малиновое", "шоколадное", "вишневое"])

    IceCreamStand1.describe_restaurant()
    IceCreamStand1.list_flavors()

    IceCreamStand2.describe_restaurant()
    IceCreamStand2.list_flavors()

def task_2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"{self.restaurant_name} открыт")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, adress, time_work):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.adress = adress
            self.time_work = time_work

        def list_flavors(self):
            print(f"Список сортов мороженого в '{self.restaurant_name}' :")
            for flavor in self.flavors:
                print(f" - {flavor}")

        def describe_restaurant(self):
            print(f"\nНазвание ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Адрес: {self.adress}")
            print(f"Время работы: {self.time_work}")

        def add_flavors(self, new_flover):
            if new_flover in self.flavors:
                print(f"Мороженое {new_flover} уже есть в списке")
            else:
                self.flavors.append(new_flover)
                print(f"Добавлен новый сорт мороженого - {new_flover}")

        def delete_flavors(self, deleted_flover):
            if deleted_flover in self.flavors:
                self.flavors.remove(deleted_flover)
                print(f"Мороженого {deleted_flover} удалено")
            else:
                print(f"Мороженое {deleted_flover} уже удалено")

        def check_flavors(self, flavor):
            if flavor in self.flavors:
                print(f"Мороженое {flavor} - в наличии")
            else:
                print(f"Мороженое {flavor} - нет в наличии")

        def IceCreamType_stick(self, flavor):
            if flavor in self.flavors:
                print(f"Мороженое {flavor} на палочке")
            else:
                print(f"Мороженое {flavor} - нет в наличии")

        def IceCreamType_waffle(self, flavor):
            if flavor in self.flavors:
                print(f"Мороженое {flavor} с вафлей")
            else:
                print(f"Мороженое {flavor} - нет в наличии")

    IceCreamStand1 = IceCreamStand("Золотая рыбка", "Кафе-мороженое", ["фисташковое", "пломбир", "шоколадное", "крем-брюле", "клубничное"], "Красноперекопская 12", "9:00-18:00")

def task_3():

    root = Tk()
    root['bg'] = 'gray'
    root.title('Кафе-мороженое')
    root.geometry('400x150')
    root.resizable(width=False, height=False)

    title = Label(text='Золотая рыбка', font=80, bg = 'grey', fg = 'white')
    title.pack()
    text1 = Label(text='Тип кухни: кафе-мороженое', font=40, bg = 'grey', fg = 'yellow')
    text1.pack()
    text2 = Label(text='Список сортов мороженого в кафе "Золотая рыбка":', font=40, bg = 'grey', fg = 'brown')
    text2.pack()
    text3 = Label(text= '- пломбир\n - шоколадное\n - клубничное', font=40, bg = 'grey', fg = 'black')
    text3.pack()

    root.mainloop()
