generator=[value-2 for value in range(1,11)]
print(generator)

print("After changing the menu")

generator= []
for value in range(1,11):
    generator=value-2
    print(generator)