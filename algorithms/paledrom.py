def is_palindrome(arg):
    b=[]
    for i in arg.lower():
        if i.isalnum():
            b.append(i)
    s = ''.join(b)
    #s = ''.join(c for c in arg.lower() if c.isalnum())
    i = 0
    j = len(s) - 1
    fag=True
    while i < j:
        if s[i] != s[j]:
            fag= False
        i += 1
        j -= 1
    if fag:
        print("Палиндром!")
    else:
        print("Не палиндром!")

flag =True
while flag:
    text = input("Ввеите текст чтобы понять полиром это или нет!\n")
    print("--Чтобы завершить программу наберите exit--")
    is_palindrome(text)
    if text == "exit":
        flag=False