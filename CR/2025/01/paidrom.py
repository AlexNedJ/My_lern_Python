def paidrom(word):
    if word.lower() == word.lower()[::-1]:
        return True
    else:
        return False

print(paidrom("шалаш"))