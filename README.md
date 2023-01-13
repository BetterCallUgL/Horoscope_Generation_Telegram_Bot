# Horoscope_Generation_Telegram_Bot

## Введение

Данный проект является лабораторной работой по предмету ООП. Это асинхронный бот, написанный на aiogram, который способен генерировать гороскопы при помощи дообученной модели RUGPT2Medium. Генерация гороскопов происходит на сервере, который коммуницирует с тг ботом при помощи очередей (RabbitMQ).


## Архитектура проекта

![](/Blank%20diagram.png)

## Структура проекта

+ ### [Telegram Bot](https://github.com/BetterCallUgL/Horoscope_Generation_Telegram_Bot/tree/main/tgbot)
  + [Bot.py](https://github.com/BetterCallUgL/Horoscope_Generation_Telegram_Bot/blob/main/tgbot/bot.py) - Запуск бота
  + [.env](https://github.com/BetterCallUgL/Horoscope_Generation_Telegram_Bot/blob/main/tgbot/.env.example) - Хранение токена
  + [Config_data](https://github.com/BetterCallUgL/Horoscope_Generation_Telegram_Bot/tree/main/tgbot/config_data) - Конфиг бота
  + [Handlers](https://github.com/BetterCallUgL/Horoscope_Generation_Telegram_Bot/tree/main/tgbot/handlers) - Хэндлеры
  + [Keyboards](https://github.com/BetterCallUgL/Horoscope_Generation_Telegram_Bot/tree/main/tgbot/keyboards) - Клавиатуры
  + [Services](https://github.com/BetterCallUgL/Horoscope_Generation_Telegram_Bot/tree/main/tgbot/services) - Клиент, который организовывает связь с сервером через очередь

+ ### [Server](https://github.com/BetterCallUgL/Horoscope_Generation_Telegram_Bot/tree/main/server)
  + [server.py]("https://github.com/BetterCallUgL/Horoscope_Generation_Telegram_Bot/blob/main/server/server.py") - код сервера
  + [generation.py](https://github.com/BetterCallUgL/Horoscope_Generation_Telegram_Bot/blob/main/server/generation.py) - класс, организующий генерацию гороскопа
