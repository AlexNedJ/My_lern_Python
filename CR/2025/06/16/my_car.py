from car import Car
from electro_car import Electric_Car as EC

my_beatle = Car('volkswagen', 'beatle', '2023')
print(my_beatle.get_deskribe_name())

my_tesla = EC('tesla', 'model X', '2024')
print(my_tesla.get_deskribe_name())
