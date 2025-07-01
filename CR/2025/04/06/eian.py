elian_0={
         'x_position': 0,
          'y_position': 25,
          'speed': 'medium',
          'points': 5
         }
print(f"Original position: {elian_0['x_position']}")

if elian_0['speed'] == 'slow':
    x_incerement = 1
elif elian_0['speed'] == 'medium':
    x_increment = 2
else:
     x_increment = 3

elian_0['x_position'] = elian_0['x_position'] + x_increment
print(f"New position: {elian_0['x_position']}")
del elian_0['points']
print(elian_0)