# Эксперимент A. Неизменяемый объект

a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))


# Эксперимент B. Изменяемый объект

first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

second = [10, 20, 30]
print(f'first == second: {first == second}')
print(f'first is second: {first is second}')

second.remove(20)
print(first, second)


# Практическая задача

from copy import deepcopy

config1 = ['First project', ['Valeria', 'Daniil'], ['--port=20', 'debug']]
config2 = config1
print('Before changing:')
print(f'config1: {config1}')
print(f'config2: {config2}', end='\n\n')

config2[1][1] = 'Ivan'
print('With mutation:')
print(f'config1: {config1}')
print(f'config2: {config2}', end='\n\n')
assert config1 is config2
assert config1[1] is config2[1]

config2 = deepcopy(config1)
config2[0] = 'Second project'
config2[2].remove('debug')
print('With deepcopy():')
print(f'config1: {config1}')
print(f'config2: {config2}')
assert config1 is not config2
assert config1[1] is not config2[1]
assert config1[2] is not config2[2]
assert 'debug' in config1[2]
assert 'debug' not in config2[2]


print('''
Итог: после config2 = config1: переменные ссылаются на один объект,
поэтому изменения затронули оба списка. Общими были сам список и
оба вложенных списка. config2 = deepcopy(config1) создал
глубокую копию, где даже вложенные списки являются разными объектами
''')