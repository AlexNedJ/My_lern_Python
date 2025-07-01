class Dog():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def sit(self):
        print(f"{self.name} is new sitings")

    def roll_over(self):
        print(f"{self.name} roll over!")

my_dog = Dog('Morgan', 15)
print(f"My dog is {my_dog.name}")
print(f"My dog is {my_dog.age} yars old.")

my_dog.sit()
my_dog.roll_over()