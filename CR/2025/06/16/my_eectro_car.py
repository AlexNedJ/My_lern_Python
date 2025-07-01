from car import Electric_Car, Car

my_tesla = Electric_Car("Tesla", "model A", ' 2020')
print(my_tesla.get_deskribe_name())
my_tesla.battery.describe_buttery()
my_tesla.battery.get_range()

my_beatle = Car('volksagen', 'beetle', ' 2018')
print(my_beatle.get_deskribe_name())