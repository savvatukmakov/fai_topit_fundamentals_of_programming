students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}


def mean(values: list[int]) -> float | None:
    """Возвращает среднее значение или None для пустого списка."""
    if not values:
        return None

    total = 0
    for value in values:
        total += value

    return total / len(values)


def minimum(values: list[int]) -> int | None:
    """Возвращает минимальное значение или None для пустого списка."""
    if not values:
        return None

    smallest = values[0]
    for value in values:
        if value < smallest:
            smallest = value

    return smallest


def maximum(values: list[int]) -> int | None:
    """Возвращает максимальное значение или None для пустого списка."""
    if not values:
        return None

    largest = values[0]
    for value in values:
        if value > largest:
            largest = value

    return largest


anna_results = students["Анна"]

print("Средний балл Анны:", mean(anna_results))
print("Минимальный балл Анны:", minimum(anna_results))
print("Максимальный балл Анны:", maximum(anna_results))
print("Среднее без оценок:", mean([]))

assert mean(anna_results) == 85.25
assert minimum(anna_results) == 78
assert maximum(anna_results) == 91

assert mean([]) is None
assert minimum([]) is None
assert maximum([]) is None
assert mean([0]) == 0.0

def classify(score: float | None) -> str:
    """Возвращает категорию среднего балла или пометку об отсутствии оценок."""
    if score is None:
        return "нет результатов"
    if score >= 90:
        return "отличный"
    if score >= 75:
        return "хороший"
    if score >= 60:
        return "удовлетворительный"
    return "недостаточный"


category_cases = [
    (None, "нет результатов"),
    (0, "недостаточный"),
    (59.9, "недостаточный"),
    (60, "удовлетворительный"),
    (74.9, "удовлетворительный"),
    (75, "хороший"),
    (89.9, "хороший"),
    (90, "отличный"),
]

print("\nПроверка категорий:")
for score, expected in category_cases:
    category = classify(score)
    print(f"{score} → {category}")
    assert category == expected

def student_summary(name: str, results: list[int]) -> dict:
    """Возвращает имя, число оценок, средний балл, минимум, максимум и категорию."""
    average = mean(results)

    return {
        "name": name,
        "count": len(results),
        "average": average,
        "minimum": minimum(results),
        "maximum": maximum(results),
        "category": classify(average),
    }


anna_summary = student_summary("Анна", students["Анна"])
empty_summary = student_summary("Без оценок", [])

print("\nСводка по Анне:", anna_summary)
print("Сводка для пустого списка:", empty_summary)

assert anna_summary["count"] == 4
assert anna_summary["average"] == 85.25
assert anna_summary["category"] == "хороший"

assert empty_summary["count"] == 0
assert empty_summary["average"] is None
assert empty_summary["category"] == "нет результатов"

def group_summary(students: dict[str, list[int]]) -> dict:
    """Возвращает число студентов и оценок, общий средний балл и счётчики категорий."""
    category_counts = {
        "отличный": 0,
        "хороший": 0,
        "удовлетворительный": 0,
        "недостаточный": 0,
        "нет результатов": 0,
    }
    total_score = 0
    score_count = 0

    for results in students.values():
        category = classify(mean(results))
        category_counts[category] += 1

        for score in results:
            total_score += score
            score_count += 1

    average = None
    if score_count > 0:
        average = total_score / score_count

    return {
        "student_count": len(students),
        "score_count": score_count,
        "average": average,
        "categories": category_counts,
    }


group_data = group_summary(students)

print("\nСтудентов в группе:", group_data["student_count"])
print("Всего оценок:", group_data["score_count"])
print(f"Средний балл группы: {group_data['average']:.2f}")
print("По категориям:", group_data["categories"])

assert group_data["student_count"] == 4
assert group_data["score_count"] == 13
assert group_data["average"] == 1032 / 13
assert group_summary({})["average"] is None

def find_top_students(students: dict[str, list[int]]) -> list[str]:
    """Возвращает имена всех студентов с наибольшим средним баллом."""
    best_average = None
    leaders = []

    for name, results in students.items():
        average = mean(results)
        if average is None:
            continue

        if best_average is None or average > best_average:
            best_average = average
            leaders = [name]
        elif average == best_average:
            leaders.append(name)

    return leaders


tied_group = {
    "Анна": [80],
    "Борис": [90, 100],
    "Дарья": [95],
}

print("Лидеры исходной группы:", find_top_students(students))
print("Лидеры при равном среднем:", find_top_students(tied_group))
print("Лидеры в группе без оценок:", find_top_students({"Илья": []}))

assert find_top_students(students) == ["Дарья"]
assert find_top_students(tied_group) == ["Борис", "Дарья"]
assert find_top_students({"Илья": []}) == []
assert find_top_students({}) == []

def build_ranking(students: dict[str, list[int]]) -> list[dict]:
    """Возвращает сводки студентов по убыванию среднего балла."""
    with_scores = []
    without_scores = []

    for name, results in students.items():
        summary = student_summary(name, results)

        if summary["average"] is None:
            without_scores.append(summary)
        else:
            with_scores.append(summary)

    with_scores.sort(key=lambda summary: summary["average"], reverse=True)
    return with_scores + without_scores


student_data = build_ranking(students)

print("\nРейтинг группы:")
for summary in student_data:
    if summary["average"] is None:
        print(f"{summary['name']}: нет результатов")
    else:
        print(f"{summary['name']}: {summary['average']:.2f} — {summary['category']}")

assert [summary["name"] for summary in student_data] == [
    "Дарья", "Анна", "Борис", "Илья"
]

def format_report(student_data: list[dict], group_data: dict) -> str:
    """Формирует текстовый отчёт по рейтингу студентов и сводке группы."""
    lines = ["Рейтинг группы:"]

    if not student_data:
        lines.append("Группа пуста")

    for summary in student_data:
        name = summary["name"]
        average = summary["average"]

        if average is None:
            lines.append(f"{name}: нет результатов")
        else:
            lines.append(
                f"{name}: средний {average:.2f}, минимум {summary['minimum']}, "
                f"максимум {summary['maximum']} — {summary['category']}"
            )

    lines.append("")
    lines.append(f"Студентов: {group_data['student_count']}")
    lines.append(f"Оценок: {group_data['score_count']}")

    group_average = group_data["average"]
    if group_average is None:
        lines.append("Средний балл группы: нет результатов")
    else:
        lines.append(f"Средний балл группы: {group_average:.2f}")

    leaders = group_data["leaders"]
    if leaders:
        lines.append("Лидеры: " + ", ".join(leaders))
    else:
        lines.append("Лидеры: нет")

    lines.append("По категориям:")
    for category, count in group_data["categories"].items():
        lines.append(f"  {category}: {count}")

    return "\n".join(lines)


group_data["leaders"] = find_top_students(students)
report = format_report(student_data, group_data)

print("\nИтоговый отчёт")
print(report)

assert "Лидеры: Дарья" in report
assert "Средний балл группы: 79.38" in report

# Название, данные группы, число оценок, средний балл группы, лидеры
scenarios = [
    ("Обычная группа", students, 13, 1032 / 13, ["Дарья"]),
    ("Один студент", {"Анна": [80, 90]}, 2, 85.0, ["Анна"]),
    ("Несколько лидеров", tied_group, 4, 91.25, ["Борис", "Дарья"]),
    ("Пустая группа", {}, 0, None, []),
    ("Студент без оценок", {"Анна": [], "Борис": [0]}, 1, 0.0, ["Борис"]),
    (
        "Границы категорий",
        {"Илья": [59], "Борис": [60], "Анна": [75], "Дарья": [90]},
        4,
        71.0,
        ["Дарья"],
    ),
]

print("\nПроверка сценариев:")

for title, group, expected_count, expected_average, expected_leaders in scenarios:
    ranking = build_ranking(group)
    summary = group_summary(group)
    leaders = find_top_students(group)
    summary["leaders"] = leaders
    text = format_report(ranking, summary)

    assert summary["student_count"] == len(group)
    assert summary["score_count"] == expected_count
    assert summary["average"] == expected_average
    assert leaders == expected_leaders

    if title == "Пустая группа":
        assert "Группа пуста" in text
        assert "Средний балл группы: нет результатов" in text

    if title == "Студент без оценок":
        assert ranking[0]["name"] == "Борис"
        assert "Анна: нет результатов" in text
        assert summary["categories"]["нет результатов"] == 1
        assert summary["categories"]["недостаточный"] == 1

    if title == "Границы категорий":
        assert [student["category"] for student in ranking] == [
            "отличный",
            "хороший",
            "удовлетворительный",
            "недостаточный",
        ]

    print(f"{title} — проверки пройдены")