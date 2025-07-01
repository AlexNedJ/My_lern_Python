favoriteNumbers={
    'Sasha':{
        'Number':[1,2,3,4,6]
    },
    'tatiana':{
        'Number':[45,88,21,9494]   
    },
    'Maria':{
        'Number':[3,2,3,2,5,0,1,32]
    }
}

for name, numbers in favoriteNumbers.items():
    print(f"Пользователь:{name},\n Любимые числа: {numbers["Number"]}")