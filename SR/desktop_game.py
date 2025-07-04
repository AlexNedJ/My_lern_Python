import tkinter as tk
import random

options = ["камень", "ножницы", "бумага", "колодец"]

def play(user_choice):
    label_result.config(text="Компьютер думает...")
    root.after(1000, lambda: show_result(user_choice))  # 1000 мс = 1 секунда

def show_result(user_choice):
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        result = "Ничья! Мыслим одинаково 🤔"
    elif (
        (user_choice == "камень" and computer_choice == "ножницы") or
        (user_choice == "ножницы" and computer_choice == "бумага") or
        (user_choice == "бумага" and computer_choice == "камень") or
        (user_choice == "колодец" and computer_choice in ["камень", "ножницы"])
    ):
        result = "Ты победил! Но это случайность... 😏"
    else:
        result = "Компьютер победил! Я же говорил, что я умнее 😎"
    label_result.config(text=f"Компьютер выбрал: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Камень, ножницы, бумага")
root.geometry("500x300")

label_title = tk.Label(root, text="Добро пожаловать в игру!", font=("Arial", 16))
label_title.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

for option in options:
    btn = tk.Button(frame, text=option.capitalize(), width=12, font=("Arial", 12),
                    command=lambda opt=option: play(opt))
    btn.pack(side=tk.LEFT, padx=5)

btn_exit = tk.Button(root, text="Выйти", command=root.destroy, font=("Arial", 12))
btn_exit.pack(pady=20)

root.mainloop()