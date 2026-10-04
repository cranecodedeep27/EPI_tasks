# Задание 6
string = "INDEX OUT OF RANGE RING ROOT"

str_lst = string.split()

count = 0
for word in str_lst:
    if word.startswith("R"):
        count += 1
        
print(count)