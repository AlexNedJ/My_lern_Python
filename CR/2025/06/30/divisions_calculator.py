
print("give me two gamnambers, and i'll divide them")
print("Enter 'n' to quit")
while True:
    First_number = input("\tFirst number:")
    if First_number == 'n':
        break
    second_number = input("second number:")
    if second_number == 'n':
        break
    try:
        answer = int(First_number) / int(second_number)
    except ZeroDivisionError:
        print("Деление на ноль запрещено математикой умнек")
    else:
        print(answer)