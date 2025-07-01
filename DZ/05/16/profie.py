def bild_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profie = bild_profile('albert','einstein', location='princeton', freld='physics', city='New Yerk')

print(user_profie)

user_profie = bild_profile('sasha','nedov', location='fontan', freld='ctudent', city='Sradessa')
print(user_profie)