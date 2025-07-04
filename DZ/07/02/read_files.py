def re(fd):
    try:
        with open(fd, 'r+', encoding= 'utf-8') as de:
         txt = de.readlines()
         print(txt)
    except FileNotFoundError:
       print("Данного файла не существует")
        
my_files = [r'd:\learning\MyPython\DZ\07\02\catss.txt', r'd:\learning\MyPython\DZ\07\02\dogs.txt']    
for file in my_files:
   re(file)
       
