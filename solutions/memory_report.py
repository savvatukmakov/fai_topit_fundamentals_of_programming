import sys
import tracemalloc

# Размеры отдельных объектов

numbers = list(range(10))

objects = [
    ("Пустой список", [], 0),
    ("Список из 10 чисел", numbers, len(numbers)),
    ("Кортеж из 10 чисел", tuple(numbers), len(numbers)),
    ("Строка из 10 символов", "abcdefghij", 10),
    ("Целое число", 10, "—"),
    ("None", None, "—"),
]

sizes = []

for name, obj, count in objects:
    sizes.append((name, count, sys.getsizeof(obj)))

# Рост списка

growing_list = []
previous_size = sys.getsizeof(growing_list)
growth = [(0, previous_size)]

for number in range(100):
    growing_list.append(number)
    current_size = sys.getsizeof(growing_list)

    if current_size != previous_size:
        growth.append((len(growing_list), current_size))
        previous_size = current_size

# Сравнение списка и range

scenarios = []

for name in ("list", "range"):
    tracemalloc.start()

    if name == "list":
        data = list(range(100000))
    else:
        data = range(100000)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    scenarios.append({
        "name": name,
        "count": len(data),
        "size": sys.getsizeof(data),
        "current": current,
        "peak": peak,
    })

    del data

peak_ratio = scenarios[0]["peak"] / scenarios[1]["peak"]

# Вывод сохранённых результатов

print("РАЗМЕРЫ ОТДЕЛЬНЫХ ОБЪЕКТОВ")
print(f"{'Объект':<25} {'Элементов':>10} {'Размер, байт':>14}")

for name, count, size in sizes:
    print(f"{name:<25} {count:>10} {size:>14}")

print("\nРОСТ СПИСКА")
print(f"{'Длина':>10} {'Размер, байт':>14}")

for count, size in growth:
    print(f"{count:>10} {size:>14}")

print("\nСРАВНЕНИЕ СПИСКА И RANGE")

for result in scenarios:
    print("\nСценарий:", result["name"])
    print("Число элементов:", result["count"])
    print("Размер внешнего объекта, байт:", result["size"])
    print(f"Текущая память: {result['current'] / 1024:.2f} КиБ")
    print(f"Пиковая память: {result['peak'] / 1024:.2f} КиБ")

print(f"\nОтношение пиков list / range: {peak_ratio:.2f}")