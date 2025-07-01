trave={}

fage=True
while fage:
    user=input("Как вас зовут\n")
    user_trave=input("Куда вы хотите отправиться отдыхать\n")
    trave[user]=user_trave
    repeat = input("Вы будете еще вводить новых пользователей (yes/no)\n")
    if repeat == 'no':
        fage=False

print("\n--- Добавленные пользователи ---")
for name, trav in trave.items():
    print(f"Имя: {name.title()}, хочет отдохнуть в: {trav.title()}")
