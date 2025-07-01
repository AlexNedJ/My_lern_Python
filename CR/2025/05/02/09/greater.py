def get_formated_name(f_name, l_name ):
    full_name=f"{f_name} {l_name}"
    return full_name.title()
while True:
    print("\nСкажи свое имя:")
    f_name=input("ИМЯ: ")
    if f_name =="exit":
        break
    l_name=input("ФАМИЛИЯ: ")
    if l_name=="exit":
        break

    formated_name= get_formated_name(f_name, l_name)
    print(f"Привет,{formated_name}!")