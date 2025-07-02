def count_worsd(filename):
    try:
        with open(filename, encoding= 'utf-8') as ff:
            contens = ff.read()
    except FileNotFoundError:
        print(f"sorry the file {filename} dosn not a exits.")
    else:
        words = contens.split()
        number_words = len(words)
        print(f"The file {filename} has abaut {number_words} words.")

filenames =[r'D:\learning\MyPython\CR\2025\06\30\litl_woman.txt',
            r'D:\learning\MyPython\CR\2025\06\30\mobidic.txt',
            r'D:\learning\MyPython\CR\2025\06\30\siddhardha.txt',] 

for fiename in filenames:
    count_worsd(fiename)

print("test")