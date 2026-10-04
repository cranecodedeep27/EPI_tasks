# Задание 5
s = "абдАыоВиеФАВбфа"
replaced_s = ""

"""Заменить все буквы а на б
и все буквы А на В"""

count = 0
for i in range(len(s)):
    if s[i] == "а":
        replaced_s += "б"
        count += 1
    elif s[i] == "А":
        replaced_s += "В"
        count += 1
    else:
        replaced_s += s[i]
        
print(replaced_s, count, sep="\n")
        