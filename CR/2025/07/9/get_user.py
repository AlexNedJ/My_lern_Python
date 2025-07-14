import json
file_Name = "number.json"
with open(file_Name) as f:
    user_name = json.load(f)
    print(f"welcom back, {user_name} ")
