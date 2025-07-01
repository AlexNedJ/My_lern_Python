file_name = r'D:\learning\MyPython\DZ\06\27\guest.txt'

try:
    flag = True
    while flag:
        guest_name = input('Почему вы любите программировать? ')

        with open(file_name, 'a') as objct_name:
            objct_name.write(f'{guest_name} \n')

        if guest_name == 'no':
            flag=False
except :
    print("no date")