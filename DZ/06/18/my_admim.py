from admin import Admin, Privilages

admim = Admin('Tatiana', 'Nedova')
admim.show_privilages()
not_my_admim = Privilages('add users')
not_my_admim.show_privilages()