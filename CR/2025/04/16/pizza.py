pizza={
    'crust': 'thick',
    'topings': ['mushrooms','extra cheesse'] ,
}

print(f"You ordered a {pizza['crust']} crust pizza "
      "with the followings toppings:")

for topping in pizza['topings']:
    print("\t " + topping)