from PIL import Image


def task_1():
    img = Image.open('2404/открытка1.jpg')

    img_photo = img.crop((50, 40, 1100, 1200))
    img_photo.show()
    img_photo.save('2404/img_photo.jpg')

    img_text = img.crop((300, 470, 1800, 1200))
    img_text.show()
    img_text.save('2404/img_text.jpg')

task_1()

def task_2():
    pictures = { "8 марта" : "2404/marth.jpg", "Новый год" : "2404/year.jpg", "День рождения" : "2404/birthday.jpg"}

    holiday = input("Введите название праздника: ")

    if holiday in pictures:
        picture_file = pictures[holiday]

        print(f"Открытка к празднику {holiday}")

        picture = Image.open(picture_file)
        picture.show()
    else:
        print("Извините, открытки к данному празднику нет")

def task_3():
    pass