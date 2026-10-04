string = input("Введите строку: ")

longest_word = max(string.split(), key=len)

print(f"Самое длинное слово: {longest_word}")
print(f"Количество букв в слове: {len(longest_word)}")
        