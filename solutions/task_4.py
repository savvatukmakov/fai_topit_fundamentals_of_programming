import gc

# Информация о сборщике мусора

print("Автоматическая сборка включена:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:", gc.get_stats())

# Цикл из двух списков

first = []
second = []

first.append(second)
second.append(first)

print("\nfirst ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

first_id = id(first)
second_id = id(second)

print("Идентификаторы списков:", first_id, second_id)

del first
del second

collected = gc.collect()

print("Найдено недостижимых объектов:", collected)

# Ручная сборка при отключённой автоматической сборке

gc.collect()
gc.disable()

try:
    print("\nАвтоматическая сборка включена:", gc.isenabled())

    for _ in range(3):
        first = []
        second = []

        first.append(second)
        second.append(first)

        del first
        del second

    collected = gc.collect()
    print("Найдено недостижимых объектов:", collected)

finally:
    gc.enable()

print("Автоматическая сборка восстановлена:", gc.isenabled())


# Циклический граф и независимый объект

collected_before = gc.collect()
print("\nСобрано перед созданием графа:", collected_before)

gc.disable()

try:
    node_a = {"name": "A", "links": []}
    node_b = {"name": "B", "links": []}
    node_c = {"name": "C", "links": []}
    node_d = {"name": "D", "links": []}

    node_a["links"].append(node_b)
    node_b["links"].append(node_c)
    node_c["links"].append(node_a)

    print("A ссылается на B:", node_a["links"][0] is node_b)
    print("B ссылается на C:", node_b["links"][0] is node_c)
    print("C ссылается на A:", node_c["links"][0] is node_a)
    print("Независимый объект:", node_d)

    del node_a
    del node_b
    del node_c

    collected_after = gc.collect()
    print("Собрано после удаления внешних ссылок:", collected_after)

    assert node_d["name"] == "D"
    assert node_d["links"] == []
    print("Независимый объект сохранился:", node_d)

finally:
    gc.enable()

print("Автоматическая сборка восстановлена:", gc.isenabled())