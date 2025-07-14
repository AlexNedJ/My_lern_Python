import json

def get_stored_user_name():
    file_name = "number.json"
    try:
        with open(file_name, encoding='utf-8') as f:
            user_name = json.load(f) 
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    else:
        return user_name
    
def get_neew_user_name():
    user_name = input("What is your namee? ")
    file_name = 'number.json'
    with open(file_name, 'w') as f:
        json.dump(user_name, f)
    return user_name
            
def geet_user():
    user_name = get_stored_user_name()
    if user_name:   
        print(f"welcom back {user_name}")
    else:
        user_name = get_neew_user_name()
        print(f"we'll remember you when you come back, {user_name}")

geet_user()