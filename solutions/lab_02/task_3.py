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


class Record:
    pass


record = Record()
print(sys.getrefcount(record))

weak_record = weakref.ref(record)
print(weak_record())
print(sys.getrefcount(record))

del record
print(weak_record())


# Практическое задание
objects = weakref.WeakValueDictionary()

r1 = Record()
r2 = Record()
r3 = Record()

objects["a"] = r1
objects["b"] = r2
objects["c"] = r3

print("Initial:", list(objects.values()))

del r3
print("Removed r3:", list(objects.values()))

del r2
print("Removed r2:", list(objects.values()))