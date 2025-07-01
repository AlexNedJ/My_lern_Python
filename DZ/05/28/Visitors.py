class Restoran():
    def __init__(self, restotant_name, cuisine_tabe):
        self.res_name= restotant_name
        self.cuis_tabe= cuisine_tabe
        self.number_serverd=0

    def describe_restarant(self):
        print(f"Name {self.res_name}")
        print(f"Cuisine {self.cuis_tabe}")

    def open_restorant(self):
        print(f"Restaurant {self.res_name} is open!")
    
    def set_number_served(self, visit):
        self.number_serverd =visit
        set_num=f'Количество посетителей {self.number_serverd} в {self.res_name}'
        return set_num
    
    def inckrement_ogin_atempt(self, num):
        if self.number_serverd < num:
            print(f"В ресторане нету мест")
        else:
            res= self.number_serverd - num
            print(f"Есть свобоные места, количество: {res}")


my_restoran = Restoran('Dominys','Pizza peperona')
print(my_restoran.res_name, my_restoran.cuis_tabe )
my_restoran.describe_restarant()
my_restoran.open_restorant()
print(my_restoran.set_number_served(10))

restoran = Restoran('Sio Gril','Sea restorant')
restoran.describe_restarant()
restoran.open_restorant()
print(restoran.set_number_served(12))
restoran.inckrement_ogin_atempt(6)