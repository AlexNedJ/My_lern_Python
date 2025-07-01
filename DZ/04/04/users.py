carennt_user=["peter", "john", "jane" "mary", "paul"]
new_users=["peter", "John",   "susan", "david", "linda", "mike", "sara"]

for user in new_users:
    if user.title() in carennt_user:# разобратся в чем проблема!
        print(f"{user} ,Это имя уже занято, выберите другое имя")
    else:
        print(f"Имя {user} доступно, вы можете использовать его.")