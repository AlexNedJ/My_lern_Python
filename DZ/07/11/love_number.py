import json

def get_stored_number_love():
    file_numbers = "number.json"
    try:
        with open(file_numbers) as f:
            user_numbers = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    else:
        return user_numbers
    
def get_new_number():
    user_number = input('Get your favorite numbers ')
    file_name = "number.json"
    with open(file_name, 'w') as ff:
        json.dump(user_number, ff)
    return user_number

def get_number():
    user_number = get_stored_number_love()
    if user_number:
        print(f"You are favorite number is {user_number}!")
    else:
        user_number = get_new_number()

get_number()