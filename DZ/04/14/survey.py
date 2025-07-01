Survey={
 'oeksandr': 'c++',
 'tatiana': 'go',
 'tatiana2': 'go',
 'tatiana3': 'go',
 'gena': 'python',
 'gena2': 'python',
 'bybek': 'c'
}

compScurvey=["bybek","gena"]

for key in Survey.keys():
    if key in compScurvey:
        print(f"{key} Не прошел/а опрос")
    else:
        print(f"{key} Прошел/а опрос!")
