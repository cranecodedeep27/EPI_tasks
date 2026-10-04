# Задание №1
string1 = input()
string2 = input()

# Соединяем две строки в новую
both_strings = string1 + string2
print(both_strings)

lenght_of_both_strings = len(both_strings)  # Длина новой строки
# Сравниваем длины первой и второй строки и выводим строку, которая длинее
len_string1 = len(string1)
len_string2 = len(string2)
if len_string1 > len_string2:
    print(string1)
elif len_string2 > len_string1:
    print(string2)
else:
    print("Строки одинаковой длины")

# Проверяем и выводим большую из строк 
if string1 > string2:
    print(string1)
elif string2 > string1:
    print(string2)
else:
    print("Строки равны")