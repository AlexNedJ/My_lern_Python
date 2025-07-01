cars=['BMW','Audi','Benz','Toyota','Honda']
print(cars)
print(sorted(cars, reverse=True))
print(cars)

def MySort(x):
    return len(x)

print("Элементов в списке: ",MySort(cars))
cars.reverse()
print(cars)
print(len(cars))