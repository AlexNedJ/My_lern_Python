class Restoran():
    def __init__(self, restotant_name, cuisine_tabe):
        self.res_name= restotant_name
        self.cuis_tabe= cuisine_tabe

    def describe_restarant(self):
        print(f"Name {self.res_name}")
        print(f"Cuisine {self.cuis_tabe}")

    def open_restorant(self):
        print(f"Restaurant {self.res_name} is open!")

if __name__ == '__main__':
    my_restoran = Restoran('Dominys','Pizza peperona')
    print(my_restoran.res_name, my_restoran.cuis_tabe )
    my_restoran.describe_restarant()
    my_restoran.open_restorant()

