class User():
    def __init__(self, firs_n, last_n):
        self.f_n = firs_n
        self.l_n = last_n
    
    def deskribe_user(self):
        print(f"User name: {self.f_n} ")
        print(f"User last name: {self.l_n} ")

    def great_user(self):
        print(f"Hello {self.f_n}")

user_name = User('Sasha','Nedov')
user_name.deskribe_user()
user_name.great_user()

user_name = User('Tatiana','Nedoova')
user_name.deskribe_user()
user_name.great_user()