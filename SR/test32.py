import random

print("Добро пожаловать в игру 'Камень, ножницы, бумага'")
print("Попробуй победить компьютер... если сможешь ")

options = ["камень", "ножницы", "бумага"]

while True:
    user_choice = input("Выбери (камень/ножницы/бумага) или 'выход' для завершения: ").lower()
    if user_choice == "выход":
        print("Убегаешь? Ладно  до встречи")
        break
    if user_choice not in options:
        print("Я не знаю такого варианта! Попробуй снова.")
        continue

    computer_choice = random.choice(options)
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья! Мыслим одинаково ")
    elif (
        (user_choice == "камень" and computer_choice == "ножницы") or
        (user_choice == "ножницы" and computer_choice == "бумага") or
        (user_choice == "бумага" and computer_choice == "камень")
        
    ):
        
        print("Ты победил! Но это случайность... ")
    
    else:
        
        print("Компьютер победил! Я же говорил, что я умнее 😎")