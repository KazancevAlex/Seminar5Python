# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = "fdfgdgf dfgdfg абвав нракк абвак"
print(f"Заданный текст: {txt}")
del_txt = "абв"
lst = [i for i in txt.split() if del_txt not in i]
print(f'Конечный текст: {lst}')