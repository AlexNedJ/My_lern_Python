
unconfirmed_users = ['aice','brain','candace']
confirmed_users=[]


while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f" Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)

print("\nThe foowing users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())