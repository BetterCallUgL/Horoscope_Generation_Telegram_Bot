from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# создаём клавиатуру с кнопками "/help" и "/generate"
help_generate_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

button_help = KeyboardButton(text='/help')
button_generate = KeyboardButton(text='/generation')

# располагаем кнопки радом друг с другом
help_generate_kb.add(button_help, button_generate)

# создаём клавиатуру с кнопками знаков зодиака
zodiacs = ['Рыбы', 'Водолей', 'Козерог', 'Стрелец', 'Скорпион', 'Весы', 'Дева', 'Лев', 'Рак', 'Близнецы', 'Телец',
           'Овен']
zodiac_kb = ReplyKeyboardMarkup(resize_keyboard=True)

# размещаем кнопки со знаками зодиака на клавиатуру
for i in range(len(zodiacs)):
    zodiac_button = KeyboardButton(text=zodiacs[i])
    if i % 3 == 0:
        zodiac_kb.add(zodiac_button)
    else:
        zodiac_kb.insert(zodiac_button)
