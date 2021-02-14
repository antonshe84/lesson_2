"""
3. *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьезнее,
чем может сначала показаться.
"""

# Объявление списка и переменных
list_diff = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
add_sign = ''
i = 0
print("Исходный список: ".ljust(25), list_diff)

# Цикл поиска чисел и обособление их кавычками
while i < len(list_diff):
    current = list_diff[i]
    if current[0] == "+" or current[0] == "-":  # Если первый символ содержит знак
        add_sign = current[0]                   # , то запоминаем знак
        current = current[1:]                   # и убираем символ знака из строки
    else:
        add_sign = ''
    if current.isdigit():                       # Если строка является целым числом
        list_diff.pop(i)
        list_diff.insert(i, '"')
        list_diff.insert(i + 1, f'{add_sign}{int(current):02d}')
        list_diff.insert(i + 2, '"')
        i += 3
    else:
        i += 1
print("Преобразованный список: ".ljust(25), list_diff)

# Формирование строки их списка для вывода
str_output = ''
i = 0
while i < len(list_diff):
    if list_diff[i] == '"':
        str_output += list_diff[i] + list_diff[i+1] + list_diff[i+2] + ' '
        i += 3
    else:
        str_output += list_diff[i] + ' '
        i += 1
print("Вывод строки из списка: ".ljust(25), str_output)