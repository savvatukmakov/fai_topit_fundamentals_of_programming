a = 1000
a = 100
c = int("1000")

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b) # выведет True
print("a is b:", a is b) #
print("a == c:", a == c) #
print("a is c:", a is c) #

#3
c = None
print("c is None:",c is None)

#4
first = "python"
second = "py" + "thon"
print(first == second)
print(first is second)