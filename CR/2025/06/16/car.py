class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_deskribe_name(self):
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name.title()
    
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