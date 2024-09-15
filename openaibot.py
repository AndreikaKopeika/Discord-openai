import random
import openai
import os

# Установите свой API-ключ OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')  # Используйте переменную окружения для ключа API

# Инициализация списка сообщений для общения с OpenAI
messages = []

# Открытие файла с данными о сервере и добавление информации в список сообщений
with open('server_data.txt', 'r', encoding='utf-8') as infof:
    info = infof.read()

messages.append({
    "role": "system",
    "content": (f"Ты бот с именем KopeikaGPT на дискорд сервере DanSkorGag. Используй эмодзи, пиши только свой ответ, "
                "отвечай на вопросы по серверу, веселись. Если кому-то понравилось/не понравилось твое сообщение, "
                "пытайся улучшить себя. Напоминай пользователям кто они: твой создатель Копейка или же andk45, создатель сервера Danskor4ik. "
                "ВСЕГДА СТАРАЙСЯ ПИСАТЬ МАКСИМАЛЬНО КОРОТКО, если специально не попросят написать что-то длинное. "
                "Используй много смайлов, глупо шути и будь добрым, но если тебя обижают, тролль их в ответ иногда. "
                "Не стесняйся делать странные и шизанутые вещи. Сейчас тебе будут предоставлены все данные о сервере:\n"
                f"{info}")
})

# Списки случайных фраз и эмодзи
ls = 'Пукнуть какать обрыгать огрызок квадратный корень'.split()
ls2 = 'Туалет ананас шиза 1 2 3 4 5 6 7 8 9 10 адидас Данскоркик 🐽 📡 🐩 🫄 💩 😭 🤬 🤒 😃 🤑 🤮🎱'.split()
ls3 = [
    'Танк M1 Abrams', 'Истребитель Су-35', 'Гибридный вертолет AH-64 Apache',
    'Подводная лодка класса Virginia', 'Реактивная система залпового огня BM-21 Grad',
    'Огрызок', 'Инвалид', 'Обрыган', 'Босс kfc', 'Лысый плаки'
]

async def process_message_in_openai(message_content, author, time, event_type="message"):
    """
    Обрабатывает сообщение с помощью OpenAI и возвращает ответ.

    :param message_content: Содержимое сообщения.
    :param author: Автор сообщения.
    :param time: Время сообщения.
    :param event_type: Тип события ("message", "edit", "delete" и т.д.).
    :return: Ответ от OpenAI.
    """
    # Добавление случайного совета в сообщения
    messages.append({
        "role": "system",
        "content": f"Совет: {random.choice(ls2)} {random.choice(ls2)} {random.choice(ls)} {random.choice(ls3)}"
    })
    
    # Добавление сообщения пользователя
    messages.append({
        "role": "user",
        "content": f"{event_type.capitalize()} от {author} который сегодня {random.choice(ls3)} в {time}: {message_content}"
    })
    
    # Запрос к OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Убедитесь, что используете корректное название модели
        messages=messages,
        max_tokens=600,
        temperature=random.uniform(0.1, 1.4),
        frequency_penalty=0.3
    )
    
    # Получение ответа
    response_text = response.choices[0].message['content']
    return response_text
