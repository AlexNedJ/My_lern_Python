import restorant
class IceCrimeStand(restorant.Restoran):
    def __init__(self, *favers):
        super().__init__(self, favers)
        self.favers = favers
    
    def iceCrimList(self):
        print(f"list ice cream {self.favers}")


myicecream = IceCrimeStand('Plombir', 'Eskimo')
myicecream.iceCrimList()
myicecream.describe_restarant()