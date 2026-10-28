import sys
import weakref

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))


# Эксперимент со слабой ссылкой

class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print("\nДо удаления сильной ссылки:")
print("Объект через слабую ссылку:", weak_record())
print("Тот же объект:", weak_record() is record)

del record

print("После удаления сильной ссылки:")
print("Объект через слабую ссылку:", weak_record())

# Практическая задача. Слабый реестр объектов

registry = weakref.WeakValueDictionary()

record_1 = Record()
record_2 = Record()
temporary_record = Record()

registry["first"] = record_1
registry["second"] = record_2
registry["third"] = temporary_record

print("\nЗаписи после регистрации:")
print(list(registry.keys()))

del temporary_record

print("После удаления сильной ссылки на третий объект:")
print(list(registry.keys()))

del record_2

print("После удаления сильной ссылки на второй объект:")
print(list(registry.keys()))

print("Первый объект доступен:", registry["first"] is record_1)