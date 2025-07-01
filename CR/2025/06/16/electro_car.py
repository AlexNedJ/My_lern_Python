from car import Car

class Battery():
    def __init__(self, battery_size = 100):
        self.battery_size = battery_size

    def describe_buttery(self):
        print(f"this car has a {self.battery_size}--kwh battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
                range = 315
        print(f"this car can go {range} milles on a full charge")

class Electric_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery= Battery()
    
    def fill_gas_tank(self):
        print(f"This car doesn't need a gas tank!")