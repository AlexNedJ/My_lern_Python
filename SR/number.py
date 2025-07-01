import random

def _the_number():
    number = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100  Попробуй угадать!")

    while True:
        guess = input("Твой вариант: ")
        attempts += 1
        try:
            guess = int(guess)
        except ValueError:
            print("Пожалуйста  введи число ")
            continue

        if guess < number:
            print("Мое число больше")
        elif guess > number:
            print("Мое число меньше")
        else:
            print(f"Поздравляю! Ты угадал число за {attempts} попыток ")
            break

if __name__ == "__main__":
    _the_number()
    