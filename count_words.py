string = input("Ввуедите строку: ")

count = 1
for i in string:
    if i == " ":
        count += 1
        
print(f"Количество слов в строке: {count}")