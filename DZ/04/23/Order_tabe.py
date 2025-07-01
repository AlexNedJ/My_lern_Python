Order=input("На сколько мест вы хотите забронировать стол?")
Order=int(Order)
if Order > 8 :
    print(f"Вам прийется поожать ")
else:
    print(f"Ваш сталик готов")