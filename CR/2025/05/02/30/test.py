class Dog():
    def __init__(self, name, breed, age, gender):
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender

    def deskribe_dog(self):
        return self.name, self.age

    
    def my_print(self, x):
        for z, y in x.items():
            print(z,y)
        
dectinary = {
    'name': 'Morgan',
    'breed': 'York',
    'age':  '15',
    'gender': 'm'
    }

sde = Dog('Morgan', 'York', '15', 'm')
sde.my_print(dectinary)
