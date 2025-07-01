class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 50

    def get_deskribe_name(self):
        long_name = f"{self.make} {self.model} {self.year}  "
        print(long_name.title()) 
    
    def rid_odometer(self):
        print(f"This car has {self.odometr_reading} mell on it")
        
    def updare_odometer(self, miles):
        if miles >= self.odometr_reading:
            self.odometr_reading = miles
        else:
            print(f"You can't roll a back an odometr")
        
    def increment_odometer(self, miles):
        self.odometr_reading += miles

    def fill_gas_tank(self):
        print(f"This car need a gas tank!")

class Electric_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery= Battery()
    
    def fill_gas_tank(self):
        print(f"This car doesn't need a gas tank!")

class Battery():
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def describe_buttery(self):
        print(f"this car has a {self.battery_size}--kwh battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
                range = 315
        print(f"this car can go {range} milles on a full charge")
    
    def upgrate_baterry(self):
        if self.battery_size < 100:
            self.battery_size = 100
            
if __name__ == "__main__":
    my_tesla = Electric_Car('Tesla','model s', '2019')
    my_tesla.get_deskribe_name()

    my_tesla.battery.get_range()
    my_tesla.battery.upgrate_baterry()
    my_tesla.battery.get_range()