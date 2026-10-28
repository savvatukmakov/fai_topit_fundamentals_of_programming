import copy

# Эксперимент А. Неизменяемый объект

a = 10
b = a

print("До изменения:")
print("Значения:", a, b)
print("Идентификаторы:", id(a), id(b))

a += 1

print("После изменения:")
print("Значения:", a, b)
print("Идентификаторы:", id(a), id(b))

# Эксперимент Б. Изменяемый объект

first = [10, 20]
second = first

print("\nДо изменения списка:")
print("Списки:", first, second)
print("Идентификаторы:", id(first), id(second))

second.append(30)

print("После добавления элемента:")
print("Списки:", first, second)
print("Идентификаторы:", id(first), id(second))

# Переназначение second на новый список с теми же элементами

second = [10, 20, 30]

print("После переназначения second:")
print("Списки:", first, second)
print("Идентификаторы:", id(first), id(second))
print("first == second:", first == second)
print("first is second:", first is second)

second.append(40)

print("После изменения нового списка:")
print("first:", first)
print("second:", second)

# Практическая задача. Конфигурации проекта

config_1 = {
    "name": "Учебный проект",
    "members": ["Савва", "Анна"],
    "settings": [["mode", "test"], ["attempts", 3]]
}

# Простое присваивание

config_2 = config_1

print("\nКонфигурации до изменений:")
print("Первая:", config_1)
print("Вторая:", config_2)

config_2["members"].append("Иван")
config_2["settings"][0][1] = "release"

print("После изменения второй конфигурации:")
print("Первая:", config_1)
print("Вторая:", config_2)
print("Один объект:", config_1 is config_2)

# Создание независимой конфигурации

config_2 = copy.deepcopy(config_1)

print("\nКонфигурации до независимых изменений:")
print("Первая:", config_1)
print("Вторая:", config_2)

config_2["name"] = "Второй проект"
config_2["members"].append("Олег")
config_2["settings"][1][1] = 5

print("После изменения независимой конфигурации:")
print("Первая:", config_1)
print("Вторая:", config_2)

assert config_1 is not config_2
assert config_1["members"] is not config_2["members"]
assert config_1["settings"] is not config_2["settings"]
assert config_1["settings"][0] is not config_2["settings"][0]
assert config_1["settings"][1] is not config_2["settings"][1]

assert config_1["name"] == "Учебный проект"
assert config_1["members"] == ["Савва", "Анна", "Иван"]
assert config_1["settings"] == [["mode", "release"], ["attempts", 3]]

print("Проверки пройдены: конфигурации и их вложенные списки независимы.")