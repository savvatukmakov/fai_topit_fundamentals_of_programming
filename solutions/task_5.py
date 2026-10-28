import sys
import tracemalloc

# Размеры объектов в байтах

empty_list = []
numbers = list(range(10))
numbers_tuple = tuple(numbers)
text = "abcdefghij"
number = 10

print("Пустой список:", sys.getsizeof(empty_list))
print("Список из 10 чисел:", sys.getsizeof(numbers))
print("Кортеж из 10 чисел:", sys.getsizeof(numbers_tuple))
print("Строка из 10 символов:", sys.getsizeof(text))
print("Целое число:", sys.getsizeof(number))
print("None:", sys.getsizeof(None))

# Изменение размера списка при добавлении элементов

growing_list = []
previous_size = sys.getsizeof(growing_list)

print("\nРост списка:")
print("Длина:", len(growing_list), "Размер:", previous_size)

for number in range(100):
    growing_list.append(number)
    current_size = sys.getsizeof(growing_list)

    if current_size != previous_size:
        print("Длина:", len(growing_list), "Размер:", current_size)
        previous_size = current_size

# Сравнение памяти списка и range

tracemalloc.start()

large_list = list(range(100000))
list_current, list_peak = tracemalloc.get_traced_memory()

tracemalloc.stop()

print("\nСписок из 100000 чисел:")
print(f"Текущая память: {list_current / 1024:.2f} КиБ")
print(f"Пиковая память: {list_peak / 1024:.2f} КиБ")

del large_list

tracemalloc.start()

number_range = range(100000)
range_current, range_peak = tracemalloc.get_traced_memory()

tracemalloc.stop()

print("\nrange из 100000 чисел:")
print(f"Текущая память: {range_current / 1024:.2f} КиБ")
print(f"Пиковая память: {range_peak / 1024:.2f} КиБ")