favorite_languases={
    'jen': ['python','ruby', 'java script', 'c#', 'java'],
    'sarah':['c'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell'],
    'sasha': ['c++']
}

for name, languases in favorite_languases.items():
    light = len(languases)
    if light <= 1:
         print(f"\n{name.title()}'s favorite languages are: \n\t{languases[0].title()}")
    else:
        print(f"\n{name.title()} favorite languages are:")

        for language in languases:
            print(f"\t{language.title()}")
