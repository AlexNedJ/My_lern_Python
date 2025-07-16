def get_formadet_name(fist, last, midle=''):
    if midle:
        full_name = f"{fist} {midle} {last}"
    else:
        full_name= f'{fist} {last}'
        
    return full_name.title()