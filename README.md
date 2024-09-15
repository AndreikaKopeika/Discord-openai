# Discord Bot с интеграцией OpenAI

## Описание проекта
Этот проект представляет собой бота для Discord, который использует OpenAI для автоматической обработки и генерации ответов на сообщения. Бот может взаимодействовать с пользователями, отвечать на их сообщения, реагировать на реакции и обрабатывать изменения и удаление сообщений в указанных каналах.

## Основные функции
- Ответы на сообщения, содержащие упоминания бота или специфические ключевые слова.
- Реакции на сообщения: лайк, дизлайк и перегенерация.
- Обработка редактирования и удаления сообщений.
- Автоматические напоминания о платеже (функция закомментирована в коде).

## Зависимости
Для работы бота необходимо установить следующие библиотеки:
- `discord.py`
- `openai`
- `python-dotenv`

### Необходимо ещё установить git. Для windows можно скачать установщик по [этой](https://github.com/git-for-windows/git/releases/download/v2.46.0.windows.1/Git-2.46.0-64-bit.exe) ссылке.

## Как запустить бота
1. **Клонируйте репозиторий (нужен git):**
   ```bash
   git clone https://github.com/AndreikaKopeika/Discord-openai.git
   ```
2. **Перейдите в директорию проекта:**
   ```bash
   cd Discord-openai
   ```
3. **Запустите файл `setup.bat`:**
   В Windows, двойным щелчком или через командную строку:
   ```bash
   start setup.bat
   ```
   Этот скрипт:
   - Установит необходимые зависимости.
   - Создаст файл `.env`, если он не существует, и запросит у вас токены.

4. **Запустите бота:**
   ```bash
   python bot.py
   ```

## Конфигурация
- **allowed_channels**: Список ID каналов, в которых бот может отправлять сообщения. Укажите здесь ID нужных каналов в коде.

## Лицензия
Этот проект распространяется под лицензией GNU General Public License v3.0 (GPL-3.0). Смотрите файл `LICENSE` для получения дополнительной информации.

## Контрибьютинг
Если у вас есть предложения по улучшению или исправлению ошибок, пожалуйста, создайте issue или pull request.

## Контакты
Если у вас есть вопросы, вы можете связаться с автором через Discord: `andk45`.
