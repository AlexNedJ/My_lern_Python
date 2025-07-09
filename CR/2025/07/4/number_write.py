import json
numbers = ['2','5','12','55','33']
file_name = 'number.json'
with open(file_name, 'a') as f:
    json.dump(numbers, f)