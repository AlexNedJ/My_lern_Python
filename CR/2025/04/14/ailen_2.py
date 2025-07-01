ailens=[]

for ailen_number in range(10):
    new_ailans={'color':'green','points': 5, 'speed': 'slow'}
    ailens.append(new_ailans)

print(ailens)

for  ailen in ailens[0:3]:
    if ailen['color'] == 'green':
       
       ailen['color'] = 'yellow'
       ailen['speed'] = 'medium'
       ailen['points'] = 10 
    elif ailen['color'] == 'yellow':
       
         ailen['color'] = 'red'
         ailen['speed'] = 'fast'
         ailen['points'] = 15 
print(ailens)