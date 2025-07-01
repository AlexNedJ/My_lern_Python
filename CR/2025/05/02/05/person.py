def name(name1, name2, age=''):
    nammes={
    "Имя": name1,
    "Фамилия": name2    
    }
    if age:
        nammes['возраст']= age
    return nammes
mysicians=name("Таня", "Недова", age=39)
print(mysicians)