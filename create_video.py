from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import os


def create_picture(text, number):
    im = Image.new('RGB', (600, 600), color=('#FAACAC'))
    # Создаем объект со шрифтом
    font = ImageFont.truetype('arial.ttf', size=30)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (175, 300),
        text[number],
        # Добавляем шрифт к изображению
        font=font,
        fill='#1C0606')
    im.save(f'images/pic{number}.jpg')


def create_video():
    for number in range(11):
        create_picture(text, number)

    directory = 'C:/Users/Student/Documents/122а/Малахов Кирилл/прогр/charging_video/images'
    files = os.listdir(directory)
    images = list(filter(lambda x: x.endswith('.jpg'), files))

    clips = [ImageClip(cl_number).set_duration(2) for cl_number in images]

    final_clip = concatenate_videoclips(clips, method='compose')
    final_clip.write_videofile('charging.mp4', fps=24)


text = ['Началась зарядка!',
        'Наклоны головы',
        'Вращения шеей',
        'Вращение плеч',
        'Вращение предплечий и рук',
        'Наклоны туловища',
        'Вращения тазом',
        'Махи ногами',
        'Упражнения на растяжку',
        'Бег на месте',
        'Отжимания', ]

for number in range(11):
    create_picture(text, number)

create_video()
