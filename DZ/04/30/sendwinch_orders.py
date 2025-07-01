sandwich=["postromi","Гамбургер","Панини","postromi","Рубен","postromi"]
finish_sandwich=[]
while 'postromi' in  sandwich:
    sandwich.remove("postromi")

for san in sandwich:
    print(san)