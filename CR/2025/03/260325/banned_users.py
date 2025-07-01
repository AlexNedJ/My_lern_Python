banned_users=['tatyana','vladimir','vitalya','vika']
users="tatyana"
if users not in banned_users:
    print(f"{users.title()},you can post response if you wish")
else:
    print(f"{users.title()},you can't post response this, You're fired!")