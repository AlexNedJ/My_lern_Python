favorit={
 'oeksandr': 'c++',
 'tatiana': 'go',
 'tatiana2': 'go',
 'tatiana3': 'go',
 'gena': 'python',
 'gena2': 'python',
 'bybek': 'c'
}

friends=["oeksandr","tatiana"]

for key in favorit.keys():
    print(f"{key.title()}")

    if key in friends:
       language= favorit[key].title()
       print(f"{key.title()}, i see you love {language}!")                     

for name in sorted(favorit.keys()):
    print(f"{name.title()},спасмбо что пользуетесь. ")

for language in favorit.values():
    print(language.title())

for language in set(favorit.values()):
    print(language)