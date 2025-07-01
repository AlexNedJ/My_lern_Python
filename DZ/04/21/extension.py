cities={
 'Odessa':{
    'country':'ukrain',
    'showplace':'bleak sea',
    'population':'2m'
 },
 'Sofia':{
    'country':'Bulgaria',
    'showplace':'cathedral Oleksandra Nevskogo',
    'population':'1,3m'   
 },
 'B_dnestrovsk':{
    'country':'Ukraine',
    'showplace':'Bilhorod-Dnistrovskyi fortress',
    'population':'50k'   
 }   
}

for city,rest in cities.items():
    print(f"\nГород:{city}")
    restes = f"Страна: {rest['country']} достопримечательность: {rest['showplace']} население: {rest ['population']}"
    print(restes)