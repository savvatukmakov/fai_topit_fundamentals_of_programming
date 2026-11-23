submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = set()
laboratories = set()
attempts_by_student = {}

best_scores = {}
attempt_counts = {}

for student, laboratory, score in submissions:
    students.add(student)
    laboratories.add(laboratory)

    if student not in attempts_by_student:
        attempts_by_student[student] = []

    attempts_by_student[student].append((laboratory, score))
    key = (student, laboratory)
    if key not in attempt_counts:
        attempt_counts[key] = 0

    attempt_counts[key] += 1

    if key not in best_scores or score > best_scores[key]:
        best_scores[key] = score

print("Студенты:", students)
print("Лабораторные работы:", laboratories)

assert students == {"anna", "boris", "daria"}
assert laboratories == {"lab_01", "lab_02"}

print("\nПопытки каждого студента:")

for student, attempts in attempts_by_student.items():
    print(student, attempts)

assert attempts_by_student["anna"] == [
    ("lab_01", 5),
    ("lab_02", 5),
    ("lab_01", 4),
]

print("\nЛучшие результаты:")

for key, score in best_scores.items():
    print(key, score)

assert best_scores[("anna", "lab_01")] == 5

print("\nКоличество попыток:")

for key, count in attempt_counts.items():
    print(key, count)

assert attempt_counts[("anna", "lab_01")] == 2
assert attempt_counts[("boris", "lab_01")] == 1
assert attempt_counts[("boris", "lab_02")] == 1

students_by_lab = {}

for student, laboratory in attempt_counts:
    if laboratory not in students_by_lab:
        students_by_lab[laboratory] = set()

    students_by_lab[laboratory].add(student)

both_labs = students_by_lab["lab_01"] & students_by_lab["lab_02"]

print("\nСдавали lab_01:", students_by_lab["lab_01"])
print("Сдавали lab_02:", students_by_lab["lab_02"])
print("Сдавали обе работы:", both_labs)

assert both_labs == {"anna", "boris"}

# Добавление новой попытки
new_submission = ("daria", "lab_02", 4)
submissions.append(new_submission)
student, laboratory, score = new_submission

students.add(student)
laboratories.add(laboratory)

if student not in attempts_by_student:
    attempts_by_student[student] = []
attempts_by_student[student].append((laboratory, score))

key = (student, laboratory)

if key not in attempt_counts:
    attempt_counts[key] = 0
attempt_counts[key] += 1

if key not in best_scores or score > best_scores[key]:
    best_scores[key] = score

if laboratory not in students_by_lab:
    students_by_lab[laboratory] = set()
students_by_lab[laboratory].add(student)

if student in students_by_lab["lab_01"] and student in students_by_lab["lab_02"]:
    both_labs.add(student)

print("\nПосле добавления записи:", new_submission)
print("Попытки Дарьи:", attempts_by_student[student])
print("Лучший балл за lab_02:", best_scores[key])
print("Число попыток за lab_02:", attempt_counts[key])
print("Сдавали обе работы:", both_labs)

assert attempts_by_student[student] == [("lab_01", 3), ("lab_02", 4)]
assert best_scores[key] == 4
assert attempt_counts[key] == 1
assert both_labs == {"anna", "boris", "daria"}

def answer_query(query):
    parts = query.split()

    match parts:
        case ["student", student]:
            if student in attempts_by_student:
                return attempts_by_student[student]
            return "Студент не найден"

        case ["best", student, laboratory]:
            key = (student, laboratory)
            if key in best_scores:
                return best_scores[key]
            return "Запись не найдена"

        case ["attempts", student, laboratory]:
            key = (student, laboratory)
            if key in attempt_counts:
                return attempt_counts[key]
            return "Запись не найдена"

        case ["completed", laboratory]:
            if laboratory in students_by_lab:
                return students_by_lab[laboratory]
            return "Лабораторная работа не найдена"

        case _:
            return "Неизвестная команда или неверное число аргументов"


queries = [
    "student anna",
    "best anna lab_01",
    "attempts boris lab_02",
    "completed lab_01",
    "best boris lab_03",
    "rating anna",
]

print("\nТекстовые запросы:")

for query in queries:
    print(query, "→", answer_query(query))