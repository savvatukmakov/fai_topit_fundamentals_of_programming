def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if not values:
        raise ValueError("Нельзя вычислить среднее пустого списка")

    total = 0.0
    for value in values:
        total += value

    return total / len(values)


print("Среднее для [2.0, 6.0]:", arithmetic_mean([2.0, 6.0]))
print("Среднее для [7.5]:", arithmetic_mean([7.5]))
print("Среднее для [-3.0, 0.0, 3.0]:", arithmetic_mean([-3.0, 0.0, 3.0]))

assert arithmetic_mean([2.0, 6.0]) == 4.0
assert arithmetic_mean([7.5]) == 7.5
assert arithmetic_mean([-3.0, 0.0, 3.0]) == 0.0

def normalize_name(name: str) -> str:
    """Убирает лишние пробелы и пишет каждую часть имени с заглавной буквы."""
    parts = name.split()

    if not parts:
        return ""

    return " ".join(parts).title()


print("Полное имя:", normalize_name("  аННа   иВАНОВА  "))
print("Одно имя:", normalize_name(name="бОРИС"))
print("Только пробелы:", repr(normalize_name("   ")))

assert normalize_name("  аННа   иВАНОВА  ") == "Анна Иванова"
assert normalize_name("бОРИС") == "Борис"
assert normalize_name("   ") == ""

def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Возвращает строку с именем студента и его средним результатом."""
    name = normalize_name(student)

    if not results:
        return f"{prefix}: {name} — нет результатов"

    average = arithmetic_mean(results)
    return f"{prefix}: {name} — {average:.{precision}f}"


default_report = build_report("  аННа  ", [4, 5])
custom_report = build_report("бОРИС", [4, 4, 5], precision=1, prefix="Средний балл")
empty_report = build_report("дарья", [])

print(default_report)
print(custom_report)
print(empty_report)

assert default_report == "Результат: Анна — 4.50"
assert custom_report == "Средний балл: Борис — 4.3"
assert empty_report == "Результат: Дарья — нет результатов"

def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    result = []

    for tag in tags:
        tag = tag.strip()

        if lowercase:
            tag = tag.lower()

        if tag and tag not in result:
            result.append(tag)

    return tuple(result)


raw_tags = [" Python ", "  ", "python", "Git"]
clean_tags = collect_tags(*raw_tags)
original_case = collect_tags("Python", "python", lowercase=False)
empty_tags = collect_tags()

print("Очищенные теги:", clean_tags)
print("С сохранением регистра:", original_case)
print("Без аргументов:", empty_tags)

assert clean_tags == ("python", "git")
assert original_case == ("Python", "python")
assert empty_tags == ()

report_options = {"precision": 1, "prefix": "Средний балл"}

report = build_report("Анна", [4, 5], **report_options)

print("Отчёт с распаковкой словаря:", report)
assert report == "Средний балл: Анна — 4.5"

course = "Основы программирования"


def show_scope():
    course = "Лабораторная № 3"

    def change_course():
        nonlocal course
        course = "Задание 4"

    print("Во внешней функции до вызова:", course)
    change_course()
    print("Во внешней функции после вызова:", course)


show_scope()
print("На уровне модуля:", course)

def add_result(value, results=[]):
    results.append(value)
    return results


print("Первый вызов:", add_result(5))
print("Второй вызов:", add_result(4))

def add_result(value, results=None):
    if results is None:
        results = []
    else:
        results = results.copy()

    results.append(value)
    return results


print("Первый вызов:", add_result(5))
print("Второй вызов:", add_result(4))

grades = [3]
print("Добавили оценку:", add_result(5, grades))
print("Исходный список:", grades)

def apply_to_results(operation, values):
    """Применяет операцию к каждому значению и возвращает новый список."""
    result = []
    for value in values:
        result.append(operation(value))
    return result


def add_one(value):
    return value + 1


scores = [3, 4, 5]

increased = apply_to_results(add_one, scores)
doubled = apply_to_results(lambda value: value * 2, scores)

print("Прибавили единицу:", increased)
print("Удвоили баллы:", doubled)
print("Исходные баллы:", scores)

assert increased == [4, 5, 6]
assert doubled == [6, 8, 10]
assert scores == [3, 4, 5]

def make_threshold_checker(threshold):
    """Создаёт функцию, которая проверяет, достиг ли балл заданного порога."""
    def check(score):
        return score >= threshold

    return check


check_60 = make_threshold_checker(60)
check_90 = make_threshold_checker(90)

print("75 баллов, порог 60:", check_60(75))
print("75 баллов, порог 90:", check_90(75))
print("90 баллов, порог 90:", check_90(90))

assert check_60(75) is True
assert check_90(75) is False
assert check_90(90) is True