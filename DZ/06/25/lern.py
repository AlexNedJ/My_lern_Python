file_path = r'd:\learning\MyPython\DZ\06\25\learning_python.txt'
with open(file_path) as l:
    txt = l.readlines()

for x in txt:
    if 'Python' in x:
        x = x.replace('Python', 'C')
    print(x)
    

 

         