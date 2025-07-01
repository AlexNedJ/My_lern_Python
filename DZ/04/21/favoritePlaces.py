favoritePlaces={
    'Sofia':{
        'name':'Oleksandr'   
    },
    'Odessa':{
        'name':'tatiana'   
    },
    'Belgorod_Dnevstrosvki':{
        'name':'Maria'
    }
}

for name, places in favoritePlaces.items():
    print(f"Имя пользователя: {places['name']}, его любимое место: {name}")