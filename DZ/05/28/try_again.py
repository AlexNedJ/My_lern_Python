class User():
    def __init__(self, firs_n, last_n):
        self.f_n = firs_n
        self.l_n = last_n
        self.login_attemps = 0

    def increment_login_attempt(self, num):
        print(f"Количество посетитилей", self.login_attemps + num)

    def reset_login_attemps(self):
        print(f"Количество посетитилей", self.login_attemps)

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

user_name.increment_login_attempt(10)
user_name.increment_login_attempt(10)
user_name.reset_login_attemps()