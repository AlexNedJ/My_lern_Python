import json
file_name = "number.json"
with open(file_name) as  ff:
    number = json.load(ff)

print(number)