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

## Как запустить/установить бота
### Видео с первым/лучшим способом:
https://github.com/user-attachments/assets/a303643f-446e-4d77-ab1e-6ee14eb3d236

### Лучший способ:
1. Скачать [Python](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe) и установить его (Вначале поставить галочку где написано про PATH)
2. Скачать [git](https://github.com/git-for-windows/git/releases/download/v2.46.0.windows.1/Git-2.46.0-64-bit.exe) и установить (просто нажимаем всё время next)
3. Скачать [установщик](https://github.com/AndreikaKopeika/Discord-openai/releases/download/installer2.3/auto_setupV2.3.bat) и запустить его. Он автоматически учтановит всё необходимое. 

### Если этот способ не заработает то скорее всего ручной тоже. НО если вы хотите попробовать ручной вам понадобиться [git](https://github.com/git-for-windows/git/releases/download/v2.46.0.windows.1/Git-2.46.0-64-bit.exe) и [Python](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)

### Ручной способ (Для продвинутых)

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

# Чтобы получить ключ API OpenAI, выполните следующие действия:

* Зарегистрируйтесь на https://platform.openai.com/;
* Перейдите на страницу [«API ключи»](https://platform.openai.com/settings/profile?tab=api-keys);
* Нажмите кнопку «Создать новый секретный ключ» и дайте ключу имя (оно может быть любым);
* Скопируйте ключ API, созданный для вашего ключа.

## Полеезные ссылки
- [Как скачать git](https://www.youtube.com/watch?v=12BIw4GdGYQ).
- [Как сделать или же получить токен бота](https://www.youtube.com/watch?v=uXl_Pi2tB2o&t=181s).
- [Скачать Python](https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe)
  
