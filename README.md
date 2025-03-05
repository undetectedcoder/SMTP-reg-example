# Система регистрации с подтверждением по email

Проект представляет собой пример системы регистрации по email.

## Особенности программы для показа системы регистрации.
- 🌈 Красочный интерфейс с использованием colorama
- 🔐 Проверка сложности пароля:
  - Минимум 8 символов
  - Заглавные и строчные буквы
  - Цифры и специальные символы
- 📧 Отправка кода подтверждения на email
- 💾 Сохранение данных в JSON-формате
- 📈 Визуализация прогресса регистрации
- 📧 Проверка почты на уникальность

## Зависимости
- Python 3.6+
- colorama (`pip install colorama`)

## Настройка
1. **SMTP-настройки** (send.py):
   ```python
   smtp_server = "smtp.gmail.com"
   smtp_port = 587
   smtp_username = "ваш_email@gmail.com"
   smtp_password = "ваш_пароль_приложения"
