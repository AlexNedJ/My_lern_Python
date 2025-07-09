def count_worsd(filename):
    try:
        with open(filename, encoding= 'utf-8') as ff:
            contens = ff.read()
    except FileNotFoundError:
        print(f"sorry the file {filename} dosn not a exits.")
    else:
        words = contens.split()
        number_words = len(words)
        res_words = words.count('the')
        print(f"The file {filename} has abaut {number_words} words. количество слов the {res_words}")

filenames =[r'd:\learning\MyPython\DZ\07\02\mobidick.txt',
            r'd:\learning\MyPython\DZ\07\02\alice.txt'] 

for fiename in filenames:
    count_worsd(fiename)