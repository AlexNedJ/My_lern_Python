file = r'D:\learning\MyPython\CR\2025\06\25\pythyn.txt'
with open(file, 'a') as filesh:
    filesh.write('I love pypathon')
    filesh.write('I love pypathon2')

with open(file, 'r') as filesh:
    txt = filesh.readlines()



print(txt)  