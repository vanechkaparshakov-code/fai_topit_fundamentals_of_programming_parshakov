import sys

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

#слабая ссылка
import weakref

class Record:
    pass

record = Record()
weak_record = weakref.ref(record)
print(weak_record())
del record
print(weak_record())

#пример
class Result:
    def __init__(self, value):
        self.value = value

def calculate(n):
    return Result(n ** 2)

result = calculate(5)
cache = weakref.ref(result)
print(cache().value)
del result
print(cache())

#практическая задача
import weakref

class Record:
    pass

record_1 = Record()
record_2 = Record()

weak_record = weakref.WeakValueDictionary()
weak_record['1'] = record_1
weak_record['2'] = record_2
weak_record['3'] = Record()

print(list(weak_record.keys()))

del record_1
print(list(weak_record.keys()))

del record_2
print(list(weak_record.keys()))










