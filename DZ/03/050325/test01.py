peoples=['Бабушка Маша','Дедушка Васю','Татьяна вредная','Папа Саша']
Me_invite='Я хотел бы пригласить вас на обед, '
Me_inviteNO=peoples[3]
print(f"{Me_invite}{peoples[0]}")
print(f"{Me_invite}{peoples[1]}")
print(f"{Me_invite}{peoples[2]}")
print(f"{Me_invite}{peoples[3]}")
print(f"'Не сможет прийти, '{Me_inviteNO}!")
my_poped=peoples.pop(3)
peoples.append('Вова')
print(f"{Me_invite}{peoples[3]}")
print("Приглашаю на обед еще троих гостей!")
peoples.insert(0,'Вика')
peoples.insert(2,'Саша')
peoples.append('Коля')
print(f"{Me_invite}{peoples[0]}")
print(f"{Me_invite}{peoples[1]}")
print(f"{Me_invite}{peoples[2]}")
print(f"{Me_invite}{peoples[3]}")
print(f"{Me_invite}{peoples[4]}")
print(f"{Me_invite}{peoples[5]}")
print(f"{Me_invite}{peoples[6]}")
message='Извините, но на обед приглашаются только два гостя!'
print(message)
message_2='был удален!'
print(peoples)
print(f"{peoples.pop()} {message_2}")
print(f"{peoples.pop()} {message_2}")
print(f"{peoples.pop()} {message_2}")
print(f"{peoples.pop()} {message_2}")
print(f"{peoples.pop()} {message_2}")

print(peoples)
print(f"{Me_invite}{peoples[0]}")
print(f"{Me_invite}{peoples[1]}")
del peoples[0]
print(peoples)