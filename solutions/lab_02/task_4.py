import gc
import sys


first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)
print('Состояние сборщика мусора:', gc.isenabled())
print('Пороги поколений:', gc.get_threshold())
print('Статистика поколений', gc.get_stats())

id_1, id_2 = id(first), id(second)
print(f'id1={id_1}, id2={id_2}')
del first, second
print('Collected:', gc.collect())

# Доп. эксперимент
gc.disable()

a1, a2 = [], []
a1.append(a2)
a2.append(a1)

b1, b2 = [], []
b1.append(b2)
b2.append(b1)

del a1, a2
del b1, b2
print('Collected:', gc.collect())
gc.enable()

# Практическая задача
gc.disable()

before = gc.collect()

a = {'name': 'A', 'dep': []}
b = {'name': 'B', 'dep': []}
c = {'name': 'C', 'dep': []}
d = {'name': 'D', 'dep': []}

a['dep'].append(b)
b['dep'].append(c)
c['dep'].append(a)

print(a, b, c, d, sep='\n')
del a, b, c

after = gc.collect()

print(f'before: {before}, after: {after}')
print(f'd={d}')

gc.enable()
