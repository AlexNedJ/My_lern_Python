class Car():
    def __init__(self ,marka, model, year):
        self.make = marka
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_deskcriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odameter(self):
        print(f"This car has {self.odometer_reading} mies on it")
    
    def update_odominetor(self, miles):
        if miles >= self.odometer_reading:
           self.odometer_reading = miles
        else:
            print("You can not roll back on odominetor")

class Electric_Car(Car):
    def __init__(self, marka, model, year):
        super().__init__(marka, model, year)
        self.buttery_size = 75

    def deskribe_buttery(self):
        print()

my_new_car = Car('audi','a5','2020')
print(my_new_car.get_deskcriptive_name())
my_new_car.update_odominetor(23)
my_new_car.read_odameter()
my_new_car.update_odominetor(13)
my_new_car.read_odameter()

my_tesla = Electric_Car('tesla', 'mode s', '2019')
print(my_tesla.get_deskcriptive_name())