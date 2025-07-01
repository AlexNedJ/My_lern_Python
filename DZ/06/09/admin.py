class User():
    def __init__(self, firs_n, last_n):
        self.f_n = firs_n
        self.l_n = last_n
    
    def deskribe_user(self):
        print(f"User name: {self.f_n} ")
        print(f"User last name: {self.l_n} ")

    def great_user(self):
        print(f"Hello {self.f_n}")

class Admin(User):
    def __init__(self, firs_n, last_n):
        super().__init__(firs_n, last_n)
        self.ferst_name = firs_n
        self.last_name = last_n
    
    def show_privilages(self):
        print(f"This user {self.ferst_name}! {self.last_name}! has a ")

class Privilages():
    def __init__(self, privilages):
        self.privilages = privilages

    def show_privilages(self):
        print(f"{self.privilages}")

admin = Admin('Sasha', 'Nedov')
admin.show_privilages()

admin = Privilages('add users')
admin.show_privilages()