# Программа, которая выводит инициалы пользователя.
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
patronamic = input("Введите отчество: ")

N_S_P = f"{surname[0].upper()}. {name[0].upper()}. {patronamic[0].upper()}."
print(f"Инициалы: {N_S_P}")
