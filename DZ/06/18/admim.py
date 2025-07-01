from user import User

class Admin(User):
    def __init__(self, firs_n, last_n):
        super().__init__(firs_n, last_n)
        self.ferst_name = firs_n
        self.last_name = last_n
    
    def show_privilages(self):
        print(f"This user {self.ferst_name}! {self.last_name}! has a ")