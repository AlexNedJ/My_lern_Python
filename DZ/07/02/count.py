print("Внеси 2 любых числа.")
while True:
    First_number = input("\tПервое число:")
    if First_number == 'e':
        break
    second_number = input("Второе число")
    if second_number == 'e':
        break
    try:
        answer = int(First_number) + int(second_number)
    except ValueError:
        print("Можно вводить только цифры и числа")
    except ZeroDivisionError:
        print("Деление на ноль запрещено математикой умнек")
    else:
        print("Результат:", answer)