import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from code_gen import code

def send_email(to_email, verification_code):
    # Настройка SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Порт
    smtp_username = "ваша почта@gmail.com"  
    smtp_password = "ваш пароль приложения"

    # Настройки письма
    from_email = "noreply"  #Тут чё хочешь меняй, не воркает
    subject = "Registration"
    body = f"Ваш код для регистрации в системе TESTREGISTRATION: {verification_code} \nЕсли вы не запрашивали код, проигнорируйте это письмо." 

    # Создание сообщения
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = None
    try:
        # Создаем SMTP соединение
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()  # сервер хеллоу
        server.starttls()  # шифруем
        server.ehlo()  # Повторный сервер хеллоу после шифрования
        
        # Логинимся
        server.login(smtp_username, smtp_password)
        
        # Отправляем письмо
        server.sendmail(from_email, to_email, msg.as_string())
        print("Письмо успешно отправлено!")
        return True
        
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
        return False
        
    finally:
        # Закрываем соединение, если оно было создано
        if server is not None:
            try:
                server.quit()
            except Exception:
                pass