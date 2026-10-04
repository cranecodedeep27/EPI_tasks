# Задание 8
string = input("Введите строку: ")
lenght = len(string)
print(lenght)

if lenght % 2 == 0:
    first_couple = string[:int(lenght / 2) ]
    second_couple = string[int(lenght / 2) :]
else:
    first_couple = string[:int(lenght / 2) + 1]
    second_couple = string[int(lenght / 2) + 1:]
    
new_string = second_couple + first_couple
print(new_string)