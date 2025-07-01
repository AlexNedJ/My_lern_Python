pizza= "\nДобавьте начинку\n"
pizza2 ="\nВы добавили "
while True:
    topings3=input(pizza)
    if topings3 == 'quit':
        break
    else:
        print(f" {pizza2}  {topings3} ")