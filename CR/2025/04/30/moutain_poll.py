responses = {}

poing_active = True

while poing_active:
    name=input("\nWhat is your name?")
    response= input("Which mountains= wolud you like to climb someday?")

    responses[name]=response

    repeat = input("Would you like to let another person respond (yes/no)")
    if repeat == 'no':
        poing_active=False

print("\n--- poll results ---")    
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")