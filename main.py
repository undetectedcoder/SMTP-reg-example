#credits: Chatgpt - design
#credits: https://github.com/undetectedcoder - Code

import re
from code_gen import code
from send import send_email
import json
import os
import time
from colorama import init, Fore, Back, Style

# Инициализация colorama
init()
#чистка консоли
def clear_console():
    """Очистка консоли для разных ОС"""
    os.system('cls' if os.name == 'nt' else 'clear')
#баннер
def print_banner():
    """Вывод красивого баннера"""
    banner = f"""
{Fore.YELLOW}
    ╔══════════════════════════════════════════════╗
    ║        ТЕСТОВАЯ СИСТЕМА РЕГИСТРАЦИИ          ║
    ╚══════════════════════════════════════════════╝
{Style.RESET_ALL}"""
    print(banner)

def print_progress():
    """Вывод прогресса регистрации"""
    print(f"\n{Fore.WHITE}╔════════════════════════════════╗")
    print(f"║      ПРОГРЕСС РЕГИСТРАЦИИ      ║")
    print(f"╚════════════════════════════════╝{Style.RESET_ALL}\n")

def print_success(message):
    """Вывод успешного сообщения"""
    print(f"{Fore.YELLOW}✓ {message}{Style.RESET_ALL}")

def print_error(message):
    """Вывод сообщения об ошибке"""
    print(f"{Fore.WHITE}✗ {message}{Style.RESET_ALL}")

def print_info(message):
    """Вывод информационного сообщения"""
    print(f"{Fore.YELLOW}ℹ {message}{Style.RESET_ALL}")

def print_loading():
    """Анимация загрузки"""
    print(f"{Fore.WHITE}Обработка", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(Style.RESET_ALL)
#Чек пароля на сложность
def check_password_strength(password):
    """Проверка сложности пароля"""
    if len(password) < 8:
        return False, "Пароль должен быть не менее 8 символов"
    
    if not re.search(r"[A-Z]", password):
        return False, "Пароль должен содержать хотя бы одну заглавную букву"
    
    if not re.search(r"[a-z]", password):
        return False, "Пароль должен содержать хотя бы одну строчную букву"
    
    if not re.search(r"\d", password):
        return False, "Пароль должен содержать хотя бы одну цифру"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Пароль должен содержать хотя бы один специальный символ"
    
    return True, "Пароль соответствует требованиям"

def is_email_unique(email):
    """Проверка уникальности почты"""
    try:
        if os.path.exists("reg/test.json"):
            with open("reg/test.json", "r") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    data = [data] if data else []
                
                for user in data:
                    if user.get("Email") == email:
                        return False
    except Exception:
        pass
    return True

def load_users():
    """Загрузка существующих пользователей"""
    try:
        if os.path.exists("reg/test.json"):
            with open("reg/test.json", "r") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    return [data] if data else []
                return data
    except Exception:
        pass
    return []

def main():
    clear_console()
    print_banner()
    print_info("Добро пожаловать в систему регистрации!")
    time.sleep(2)  # Пауза для чтения приветствия
    
    clear_console()
    print_banner()
    print_progress()
    print(f"{Fore.YELLOW}[Шаг 1 из 4]{Style.RESET_ALL} Создание учетной записи")
    Login = input(f"{Fore.WHITE}Введите логин: {Style.RESET_ALL}")
    time.sleep(1)  # Пауза перед очисткой консоли
    #чистка консоли и принт баннера и прогресса
    clear_console()
    print_banner()
    print_progress()
    print(f"{Fore.YELLOW}[Шаг 2 из 4]{Style.RESET_ALL} Создание пароля")
    print_info("Требования к паролю:")
    print(f"{Fore.WHITE} • Минимум 8 символов")
    print(" • Минимум одна заглавная буква")
    print(" • Минимум одна строчная буква")
    print(" • Минимум одна цифра")
    print(f" • Минимум один специальный символ{Style.RESET_ALL}")
    
    while True:
        password = input(f"\n{Fore.WHITE}Введите пароль: {Style.RESET_ALL}")
        is_valid, message = check_password_strength(password)
        if is_valid:
            print_success(message)
            time.sleep(1)
            break
        print_error(message)
        print_info("Пожалуйста, попробуйте другой пароль")
        time.sleep(2)
    
    clear_console()
    print_banner()
    print_progress()
    print(f"{Fore.YELLOW}[Шаг 3 из 4]{Style.RESET_ALL} Привязка электронной почты")
    while True:
        Email = input(f"{Fore.WHITE}Введите свою почту: {Style.RESET_ALL}")
        if not is_email_unique(Email):
            print_error("Этот email уже зарегистрирован")
            time.sleep(2)
            continue
        break

    clear_console()
    print_banner()
    print_progress()
    print(f"{Fore.YELLOW}[Шаг 4 из 4]{Style.RESET_ALL} Подтверждение почты")
    print_loading()
    
    if send_email(Email, code):
        verification_code = input(f"{Fore.WHITE}Введите код подтверждения: {Style.RESET_ALL}")

        if verification_code == code:
            print_loading()
            print_success("Код подтверждения верный!")
            time.sleep(1)
            
            users = load_users()
            user_data = {
                "Login": Login,
                "Password": password,
                "Email": Email
            }
            users.append(user_data)
            
            with open("reg/test.json", "w") as file:
                json.dump(users, file, indent=4)
            
            clear_console()
            print_banner()
            print("\n" + "=" * 50)
            print_success("Регистрация успешно завершена!")
            print(f"\n{Fore.YELLOW}Данные учетной записи:{Style.RESET_ALL}")
            print(f"{Fore.WHITE}• Логин: {Login}")
            print(f"• Email: {Email}{Style.RESET_ALL}")
            print("\n" + "=" * 50 + "\n")
            time.sleep(5)  # Пауза для чтения финальной информации
        else:
            print_error("Неверный код подтверждения")
            time.sleep(2)
    else:
        print_error("Не удалось отправить код подтверждения")
        time.sleep(2)

if __name__ == "__main__":
    main()



