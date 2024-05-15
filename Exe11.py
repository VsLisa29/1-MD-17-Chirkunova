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

    newRestaurant = Restaurant("Ромашка", "Испанская")

    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()


def task_2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}\n")

    newRestaurant1 = Restaurant("КлодМонэ", "Французская")
    newRestaurant2 = Restaurant("Гости", "Японская")
    newRestaurant3 = Restaurant("Ромашка", "Русская")

    newRestaurant1.describe_restaurant()
    newRestaurant2.describe_restaurant()
    newRestaurant3.describe_restaurant()


def task_3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}\n")

        def open_restaurant(self):
            print(f"{self.restaurant_name} открыт")

        def updated_rating(self, update_rating):
            self.rating = update_rating
            self.describe_restaurant()

    newRestaurant1 = Restaurant("КлодМонэ", "Французская", rating=5)
    newRestaurant2 = Restaurant("Гости", "Японская", rating=2)
    newRestaurant3 = Restaurant("Ромашка", "Русская", rating=3)

    newRestaurant1.describe_restaurant()  #если не меняем рейтинг
    newRestaurant2.updated_rating(3)  #если меняем рейтинг
    newRestaurant3.updated_rating(4)