age = "Введите свой возраст\n"

while True: 
    far = input(age)
    if far == 'quit':
        break
    far= int(far)
    if far <= 3:
        print(f"Вам {far} лет, Вход бесплатно!")
        continue
    if far <=12:
        print(f"Вам {far} лет, Вход 10$") 
        continue
    if far < 95:
        print(f"Вам {far} лет, Вход 15$")  
        continue 
    if far > 95:
        print(f"Вам {far} лет, Столько не живут;)")
        continue