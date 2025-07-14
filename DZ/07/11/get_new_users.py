import json

def get_stored_user_names():
    file_name = "number.json"
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []
    return users

def add_new_user_name():
    user_name = input("What is your name? ")
    users = get_stored_user_names()
    users.append(user_name)
    with open("number.json", 'w', encoding='utf-8') as f:
        json.dump(users, f)
    return user_name

def greet_user():
    users = get_stored_user_names()
    if users:
        last_user = users[-1]
        es_name = input(f'Is your name {last_user}? Yes or No: ')
        if es_name.lower() == 'no':
            user_name = add_new_user_name()
            print(f"We'll remember you when you come back, {user_name}!")
        else:
            print(f"Welcome back, {last_user}!")
    else:
        user_name = add_new_user_name()
        print(f"We'll remember you when you come back, {user_name}!")

greet_user()