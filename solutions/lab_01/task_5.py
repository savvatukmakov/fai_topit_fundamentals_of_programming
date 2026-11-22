"""Программа создаёт информационную карточку вычислительного эксперимента."""

#1. Ввод данных

researcher = input("Имя исследователя: ")
experiment = input("Название эксперимента: ")
runs = int(input("Количество выполненных запусков: "))
duration = float(input("Длительность одного запуска в секундах: "))
real = float(input("Действительная часть коэффициента: "))
imag = float(input("Мнимая часть коэффициента: "))

#2. Вычисления

total_seconds = runs * duration
total_minutes = total_seconds / 60
coefficient = complex(real, imag)
modulus_squared = real ** 2 + imag ** 2
has_runs = bool(runs)

#3. Вывод карточки

print()
print("========================================")
print(f"ЭКСПЕРИМЕНТ: {experiment}")
print(f"Исследователь: {researcher}")
print(f"Запуски: {runs}")
print(f"Общее время: {total_seconds:.2f} с ({total_minutes:.2f} мин)")
print(f"Коэффициент: {coefficient}")
print(f"Квадрат модуля: {modulus_squared:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("========================================")
#4. Типы введённых значений
print("Типы:", type(researcher), type(experiment), type(runs), type(duration), type(real), type(imag))