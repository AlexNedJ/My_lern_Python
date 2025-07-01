def chars_count(text, char):
    # Так как ищем сумму, то начальное значение 0
    n = 0
    for current_char in text:
        # приводим все к нижнему регистру,
        # чтобы не зависеть от текущего регистра
        if current_char.lower() == char.lower():
            n += 1 # n=n+1
    return n

print(chars_count('HeXlet!', 'e'))  # 2
chars_count('hExlet!', 'e')  # 2
chars_count('hExlet!', 'E')  # 2

chars_count('hexlet!', 'a')  # 0