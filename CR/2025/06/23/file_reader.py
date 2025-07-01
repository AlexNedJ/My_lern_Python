file_path ='d:\\learning\\MyPython\\CR\\2025\\06\\23\\pi_digits.txt' 
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
bithday = input("Enter your birthday, in the form mmddyy")
if bithday in pi_string:
    print(' Your birthday appears in the first million digits on pi!.')
else:
    print(" Your birthday does not apper in the first million digits on pi.")