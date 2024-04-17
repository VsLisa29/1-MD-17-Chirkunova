from PIL import Image, ImageFilter
def task_1():
    img = Image.open('дом.jpg')
    img.show()

    print(f"Размер изображения: {img.size}")
    print(f"Формат изображения: {img.format}")
    print(f"Цветовая модель изображения: {img.mode}")

def task_2():
    img = Image.open('дом.jpg')
    res_img = img.reduce(3)
    res_img.save('дом3.jpg')

    img_rotated = img.transpose(Image.FLIP_LEFT_RIGHT)
    img_rotated.save('дом_гор.jpg')

    img_rotated = img.transpose(Image.FLIP_TOP_BOTTOM)
    img_rotated.save('дом_верт.jpg')


def task_3():
    for i in range(1,6):
        img = Image.open(f'Новая папка/{i}.jpg')
        filt_img = img.filter(ImageFilter.CONTOUR)
        filt_img.save(f'Новая папка2/фильтр{i}.jpg')

def task_4():
    img = Image.open('дом.jpg').convert('RGB')
    water = Image.open('вод.jpg').convert('RGB')
    img.paste(water, (0, 0), water)
    img.save('дом_вод.jpg')

