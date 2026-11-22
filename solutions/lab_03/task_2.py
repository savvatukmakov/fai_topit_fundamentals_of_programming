measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

total = 0
minimum = measurements[0]
maximum = measurements[0]
even_count = 0

for value in measurements:
    total += value

    if value < minimum:
        minimum = value

    if value > maximum:
        maximum = value

    if value % 2 == 0:
        even_count += 1

print("Сумма:", total)
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Количество чётных:", even_count)

# Подсчёт измерений выше среднего
average = total / len(measurements)
above_average_count = 0

for value in measurements:
    if value > average:
        above_average_count += 1

print("Среднее арифметическое:", average)
print("Количество значений выше среднего:", above_average_count)

def linear_search(values, target):
    comparisons = 0

    for index in range(len(values)):
        comparisons += 1
        if values[index] == target:
            return index, comparisons

    return -1, comparisons


target = int(input("\nВведите число для поиска: "))
index, comparisons = linear_search(measurements, target)

print("Индекс первого вхождения:", index)
print("Количество сравнений:", comparisons)

def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


print("\nПроверка чисел на простоту:")

for number, expected in [(1, False), (2, True), (29, True), (49, False)]:
    result = is_prime(number)
    print(f"{number}: {result}")
    assert result == expected

def selection_sort(values):
    for i in range(len(values) - 1):
        min_index = i

        for j in range(i + 1, len(values)):
            if values[j] < values[min_index]:
                min_index = j

        if min_index != i:
            values[i], values[min_index] = values[min_index], values[i]


sorted_measurements = measurements.copy()
selection_sort(sorted_measurements)

print("\nПосле сортировки выбором:", sorted_measurements)
assert sorted_measurements == [7, 9, 11, 12, 15, 15, 18, 18, 18, 21]

def binary_search(values, target):
    left = 0
    right = len(values) - 1
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2
        value = values[middle]

        comparisons += 1
        if value == target:
            return middle, comparisons

        comparisons += 1
        if value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1, comparisons


print("\nБинарный поиск:")

for target in (15, 21, 20):
    index, comparisons = binary_search(sorted_measurements, target)
    print(f"Число: {target}, индекс: {index}, сравнений: {comparisons}")

    if target == 20:
        assert index == -1
    else:
        assert 0 <= index < len(sorted_measurements)
        assert sorted_measurements[index] == target

# Сравнение линейного и бинарного поиска
print("\nКоличество сравнений при поиске последнего элемента")
print(f"{'Размер':>8} {'Ищем':>8} {'Линейный':>12} {'Бинарный':>12}")

for size in (10, 100, 1000):
    values = list(range(1, size + 1))
    target = size

    linear_index, linear_comparisons = linear_search(values, target)
    binary_index, binary_comparisons = binary_search(values, target)

    assert linear_index == size - 1
    assert binary_index == size - 1

    print(f"{size:>8} {target:>8} {linear_comparisons:>12} {binary_comparisons:>12}")