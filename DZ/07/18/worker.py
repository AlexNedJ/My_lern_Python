class Employ():
    def __init__(self, first_name, last_name, otklad):
        self.first_name=first_name
        self.last_name=last_name
        self.otklad = int(otklad)

    def give_rise(self, amount=5000):
        self.otklad += amount