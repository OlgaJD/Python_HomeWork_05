# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

## V1
text = input('Введите текст из которого будем удалять:\n')
text = text.split()
new_text = list(filter(lambda x: 'абв' not in x, text))
print(new_text)


# ====================================================
# # V2
# def x(i):
#     return 'абв' not in i

# text = input('Введите текст из которого будем удалять:\n')
# text = text.split()
# new_text = list(filter(x, text))
# print(new_text)