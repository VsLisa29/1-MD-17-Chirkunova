from PIL import Image


def task_1():
    img = Image.open('2404/открытка1.jpg')

    img_photo = img.crop((50, 40, 1100, 1200))
    img_photo.show()
    img_photo.save('2404/img_photo.jpg')

    img_text = img.crop((1100, 169, 1870, 780))
    img_text.show()
    img_text.save('2404/img_text.jpg')

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
    img_sign = Image.open('2404/знак.png')
    sign = img_sign.crop((0, 271, 1023, 745))
    sign = sign.reduce((2))
    sign.save('2404/новый_знак.png')

    sign = Image.open('2404/новый_знак.png')
    img_basic = Image.open('2404/кот.png')

    img_basic1 = img_basic.copy()
    img_basic1.paste(sign, (1160,120))
    img_basic1.save('2404/cat_paste.png')
    img_basic1.show()
