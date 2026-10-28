import copy

original = [
    ["Python", 5],
    ["Algorithms", 4]
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

print("До изменений:")
print("original:", original)
print("alias:", alias)
print("shallow:", shallow)
print("deep:", deep)

print("\nИдентификаторы внешних списков:")
print("original:", id(original))
print("alias:", id(alias))
print("shallow:", id(shallow))
print("deep:", id(deep))

print("\nИдентификаторы первого вложенного списка:")
print("original:", id(original[0]))
print("alias:", id(alias[0]))
print("shallow:", id(shallow[0]))
print("deep:", id(deep[0]))

print("\nИдентификаторы первой оценки:")
print("original:", id(original[0][1]))
print("alias:", id(alias[0][1]))
print("shallow:", id(shallow[0][1]))
print("deep:", id(deep[0][1]))

# Добавление нового вложенного списка

original.append(["Databases", 5])

print("\nПосле добавления предмета:")
print("original:", original)
print("alias:", alias)
print("shallow:", shallow)
print("deep:", deep)

# Изменение оценки в первом вложенном списке

original[0][1] = 3

print("\nПосле изменения оценки:")
print("original:", original)
print("alias:", alias)
print("shallow:", shallow)
print("deep:", deep)

print("\nИдентификаторы первой оценки после изменения:")
print("original:", id(original[0][1]))
print("alias:", id(alias[0][1]))
print("shallow:", id(shallow[0][1]))
print("deep:", id(deep[0][1]))

# Матрица с общими строками

wrong_matrix = [[0] * 3] * 3

print("\nМатрица с общими строками:")
print("До изменения:", wrong_matrix)
print("Идентификаторы строк:")
for row in wrong_matrix:
    print(id(row))

wrong_matrix[0][0] = 1

print("После изменения:", wrong_matrix)

# Матрица с независимыми строками

correct_matrix = [[0] * 3 for _ in range(3)]

print("\nМатрица с независимыми строками:")
print("До изменения:", correct_matrix)
print("Идентификаторы строк:")
for row in correct_matrix:
    print(id(row))

correct_matrix[0][0] = 1

print("После изменения:", correct_matrix)