def classify_record(score, work_type, absences):
    if not (0 <= score <= 100):
        return "Ошибка: результат должен быть от 0 до 100.", None
    elif not (0 <= absences <= 5):
        return "Ошибка: количество пропусков должно быть от 0 до 5.", None
    else:
        if score >= 90:
            level = "отличный"
        elif score >= 75:
            level = "хороший"
        elif score >= 60:
            level = "удовлетворительный"
        else:
            level = "недостаточный"

        if absences > 3:
            if level == "отличный":
                level = "хороший"
            elif level == "хороший":
                level = "удовлетворительный"
            elif level == "удовлетворительный":
                level = "недостаточный"

        match work_type:
            case "exam":
                description = "экзаменационная работа"
            case "project":
                description = "проектная работа"
            case "practice":
                description = "практическая работа"
            case _:
                description = "неизвестный тип работы"

        return description, level


score = int(input("Введите результат студента: "))
work_type = input("Введите тип работы (exam, project, practice): ")
absences = int(input("Введите количество пропусков: "))

description, level = classify_record(score, work_type, absences)

if level is None:
    print(description)
else:
    print("Тип работы:", description)
    print("Итоговый уровень:", level)


# Проверка граничных баллов
test_cases = [
    (0, "exam", 5, "недостаточный"),
    (59, "exam", 0, "недостаточный"),
    (60, "exam", 0, "удовлетворительный"),
    (74, "exam", 0, "удовлетворительный"),
    (75, "exam", 0, "хороший"),
    (89, "exam", 0, "хороший"),
    (90, "exam", 3, "отличный"),
    (100, "exam", 4, "хороший"),
]

print("\nПроверка граничных баллов:")

for score, work_type, absences, expected_level in test_cases:
    description, level = classify_record(score, work_type, absences)
    print(f"Балл: {score}, пропуски: {absences}, "
          f"ожидалось: {expected_level}, получено: {level}")
    assert level == expected_level

# Обработка результатов группы
records = [
    (95, "exam", 0),
    (90, "project", 4),
    (82, "practice", 2),
    (75, "exam", 5),
    (74, "project", 0),
    (60, "practice", 4),
    (59, "exam", 1),
    (0, "project", 5),
    (100, "practice", 3),
    (89, "test", 0),
]

level_counts = {
    "отличный": 0,
    "хороший": 0,
    "удовлетворительный": 0,
    "недостаточный": 0,
}

print("\nИндивидуальные результаты:")

for score, work_type, absences in records:
    description, level = classify_record(score, work_type, absences)

    if level is None:
        result = f"Балл: {score}, пропуски: {absences}. {description}"
    else:
        result = f"Балл: {score}, пропуски: {absences}. {description}, уровень: {level}"
        level_counts[level] += 1

    print(result)

print("\nИтоговая сводка:")

for level, count in level_counts.items():
    print(f"{level}: {count}")