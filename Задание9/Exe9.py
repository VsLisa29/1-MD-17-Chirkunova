import os, csv
from PIL import Image, ImageFilter

def task_1():
    input_directory1 = 'input_directory1'
    output_directory = 'output_directory'

    for filename in os.listdir(input_directory1):
        input_path = os.path.join(input_directory1, filename)
        output_path = os.path.join(output_directory, filename)

        if os.path.isfile(input_path):
            img = Image.open(input_path)
            filt_img = img.filter(ImageFilter.SHARPEN)
            filt_img.save(output_path)


def task_2():
    input_directory2 = 'input_directory2'
    output_directory = 'output_directory'

    for filename in os.listdir(input_directory2):
        input_path = os.path.join(input_directory2, filename)
        output_path = os.path.join(output_directory, filename)

        if os.path.isfile(input_path) and filename.lower().endswith(('.jpg', '.png', '.bmp')):
            img = Image.open(input_path)
            filt_img = img.filter(ImageFilter.SHARPEN)
            filt_img.save(output_path)

def task_3():
    with open('file.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        print('Нужно купить:')

        sum = 0

        for row in reader:
            kol = int(row[1])
            price = int(row[2])
            sum += kol * price

            print(f'{row[0]} - {kol} шт. за {price} руб.')

        print(f'Итоговая сумма: {sum} руб')