from name_funcions import get_formadet_name
print(f"Введите q если хотите выйти")
while True:
    fist = input("Пожалуйста введите свое имя: ")
    if fist == 'q':
        break
    last = input('Пожалуйста введите свою фамилию: ')
    if fist == 'q':
        break
    formadet_name = get_formadet_name(fist, last)
    print(f"\tNeatly formatted name: {formadet_name}")