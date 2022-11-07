# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# ## ==================================================================================
def encoding(text):
    encoding_text = "" 
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        encoding_text += str(count) + text[i]
        i += 1
 
    return encoding_text

# ## ==================================================================================
def decoding(readtxt):
    count = ''
    decoded_str = ''
    for i in range(len(readtxt)):
        if not readtxt[i].isalpha():
            count += readtxt[i]
        else:
            decoded_str += readtxt[i] * int(count)
            count = ''
    return decoded_str

# ##  ==================================================================================

## Считываем строку в отдельный файл для дальнейшего шифрования и расшифровки
with open('work_text.txt', 'w', encoding='utf-8') as f:
    new_text = f.write(input('Введите текст, который будет храниться в файле, будем работать с ним. Пример: qqwwwer: '))
    print('Готово, исходный текст записан в файл "work_text.txt"')

## Считываем строку из рабочего файла и зашифровываем и записываем в файл 'encode.txt'
with open('work_text.txt', 'r', encoding='utf-8') as f:
    with open ('encode.txt', 'w') as f1:
        f1.write(encoding(f.read()))
        print('Зашифрованный текст записан в файл "encode.txt"')
    
## Считываем зашифрованную строку из файла и расшифровываем в 'decode.txt'
with open('encode.txt', 'r', encoding='utf-8') as f:
    with open ('decode.txt', 'w') as f1:
        f1.write(decoding(f.read()))  
        print('Расшифрованный текст записан в файл "decode.txt"')