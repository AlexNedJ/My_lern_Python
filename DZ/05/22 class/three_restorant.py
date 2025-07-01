class Restoran():
    def __init__(self, restotant_name, cuisine_tabe):
        self.res_name= restotant_name
        self.cuis_tabe= cuisine_tabe

    def describe_restarant(self):
        print(f"Name {self.res_name}")
        print(f"Cuisine {self.cuis_tabe}")

    def open_restorant(self):
        print(f"Restaurant {self.res_name} is open!")

my_restoran = Restoran('Dominys','Pizza peperona')
rest_sio = Restoran('Sio grill',"Medium chicken")
rest_chicken = Restoran('Mac','burger')

my_restoran.describe_restarant()
rest_sio.describe_restarant()
rest_chicken.describe_restarant()
