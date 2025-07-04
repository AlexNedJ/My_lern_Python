import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print("="*50)
    print("   Добро пожаловать в игру 'Камень, ножницы, бумага'   ".center(50))
    print("="*50)
    print("Попробуй победить компьютер... если сможешь 😏\n")

options = ["камень", "ножницы", "бумага", "колодец"]

try:
    while True:
        clear_screen()
        print_title()
        user_choice = input("Выбери (камень/ножницы/бумага/колодец) или 'выход' для завершения: ").lower()
        if user_choice == "выход":
            print("Убегаешь? Ладно, до встречи!")
            break
        if user_choice not in options:
            print("Я не знаю такого варианта! Попробуй снова.")
            input("Нажми Enter для продолжения...")
            continue

        computer_choice = random.choice(options)
        print(f"\nКомпьютер выбрал: {computer_choice}")

        if user_choice == computer_choice:
            print("Ничья! Мыслим одинаково 🤔")
        elif (
            (user_choice == "камень" and computer_choice == "ножницы") or
            (user_choice == "ножницы" and computer_choice == "бумага") or
            (user_choice == "бумага" and computer_choice == "камень") or
            (user_choice == "колодец" and computer_choice == "бумага")
        ):
            print("Ты победил! Но это случайность... 😏")
        else:
            print("Компьютер победил! Я же говорил, что я умнее 😎")
        input("\nНажми Enter для следующего раунда...")
except EOFError:
    print("Нельзя писать знаки")