cars=['BMW','Audi','Toyota','Honda']
print(cars)
cars.append('ford')
print(cars)
print(cars[0])
poped_car=cars.pop(2)
print("я удалил  ",poped_car)
print(cars)
print(sorted(cars, reverse=True))
print(len(cars))
print(cars[-1])