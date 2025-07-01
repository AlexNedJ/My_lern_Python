def great_users(names):
    for name in names:
        msg=f"hello, {name.title()}!"
        print(msg)

user_names=["Sasha","Andrey","Margaritos"]
great_users(user_names)