student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

#1
print(student[0],student[-1])

#2
print(student[:4])
print(student[5:])

#3
print(student.upper())
print(student.lower())

#4
print(student[0]+"."+student[5]+".")

#5
print(course[::-1])

#6
print("%s - %s: %d/%d (%.1f%%)" % (student, course, completed, total,completed / total * 100))
print("{} - {}: {}/{} ({}%)".format(student, course, completed, total,completed / total * 100))
print(f"{student} - {course}: {completed}/{total} ({completed / total * 100}%)")

#7
symbol = "Я"
print(symbol)
print(ord(symbol))
print(chr(ord(symbol)))
print(symbol.encode("utf-8"))
print(len(symbol.encode("utf-8")))
print(len(symbol))

#8
"student"[0]="1"