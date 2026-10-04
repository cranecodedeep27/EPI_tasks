# Задиние 11 База данных
employees = [
    {
        "фамилия": "Иванов", 
        "год": 1981, 
        "оклад": 90000,
        "дети": 2,
        "стаж": 16
    },
    {
        "фамилия": "Петров", 
        "год": 2000, 
        "оклад": 85000,
        "дети": 1,
        "стаж": 8
    },
    {"фамилия": "Сидоров", "год": 1990, "оклад": 93000,"дети": 2,"стаж": 10},
    {
        "фамилия": "Морозов", 
        "год": 1965, 
        "оклад": 100000,
        "дети": 2,
        "стаж": 28
    },
    {
        "фамилия": "Кузнецова", 
        "год": 2001, 
        "оклад": 84000,
        "дети": 1,
        "стаж": 8
    },
    {"фамилия": "Смирнов", "год": 1976, "оклад": 87000,"дети": 3,"стаж": 22}, 
    {
        "фамилия": "Исаев", 
        "год": 1966, 
        "оклад": 91000,
        "дети": 2,
        "стаж": 30
    }, 
    {
        "фамилия": "Соколова", 
        "год": 1995, 
        "оклад": 89000,
        "дети": 3,
        "стаж": 13
    }, 
    {"фамилия": "Новиков", "год": 2002, "оклад": 70000,"дети": 0,"стаж": 8}, 
    {
        "фамилия": "Федосеев", 
        "год": 1980, 
        "оклад": 83000,
        "дети": 2,
        "стаж": 16
    }
]

# Фамилия самого взрослого:
oldest_employee = employees[0]
for employee in employees:
    if employee["год"] < oldest_employee["год"]:
        oldest_employee = employee
print(f"Самый взрослый: {oldest_employee["фамилия"]}")

# Фамилия сотрудника с самым большим стажем:
big_experience = employees[0]
for employee in employees:
    if employee["стаж"] > big_experience["стаж"]:
        big_experience = employee
print(f"Работник с самым большим стажем: {big_experience['фамилия']}")

#Средний оклад:
summary_salary = 0
for employee in employees:
    summary_salary += employee["оклад"]
print(f"средний оклад: {summary_salary / 10}")

# фамилии многодетных сотрудников:
large_families = []
for employee in employees:
    if employee["дети"] > 2:
        large_families.append(employee["фамилия"])
print(f"фамилии многодетных работников: {large_families}")

# Заменить фамилию сотрудника на новую:

old_last_name = input()
new_last_name = input()
# Cначала убедится , что работник есть в базе и изменить его фамилию
flag = False
for employee in employees:
    if employee["фамилия"] == old_last_name:
        employee["фамилия"] = new_last_name
        flag = True
        print(f"Фамилия сотрудника {old_last_name} успешно заменена на {new_last_name}")
        break
if flag == False:
    print("Такой сотрудник не найден в базе данных")
        