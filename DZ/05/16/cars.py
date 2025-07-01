def make_car(brend, model, **ese):
    ese['brend'] = brend
    ese['model'] = model
    return ese

car= make_car("subary", "outbok", coor="bue", tow_packed=True)
print(car)