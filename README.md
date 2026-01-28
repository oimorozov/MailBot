# MailBot

Простой Telegram-бот для чтения тем писем из Yandex через IMAP.

## Установка

1. **Клонируйте проект и создайте виртуальное окружение**
   ```bash
   cd MailBot
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```
   Если используете `uv`:
   ```bash
   uv sync
   ```

3. **Создайте файл `.env`**
   Пример:
   ```env
   BOT_TOKEN=ваш_токен_бота
   USER_ID=ваш_id_пользователя_тг
   USER_NAME=ваш_почтовый_логин
   IMAP_PASS=пароль_приложения_или_пароль_почты
   ```

4. **Проверьте `config.py`**
   Убедитесь, что переменные читаются из `.env`:
   - `BOT_TOKEN`
   - `USER_ID`
   - `USER_NAME`
   - `IMAP_PASS`

5. **Запуск бота**
   ```bash
   python bot.py
   ```

## Быстрый гайд по настройке

- **BOT_TOKEN** — токен Telegram-бота (получить у @BotFather)
- **USER_ID** — ID пользователя в ТГ
- **USER_NAME** — логин почты Yandex
- **IMAP_PASS** — пароль приложения

После запуска напишите боту команду `/get_mail`.
