import sys
import tracemalloc


# Часть 1
print(f'empty list: {sys.getsizeof([])}')
print(f'list (len=10): {sys.getsizeof(list(range(1, 11)))}')
print(f'tuple: {sys.getsizeof(tuple(range(1, 11)))}')
print(f'str (len=10): {sys.getsizeof("abcdefghij")}')
print(f'int: {sys.getsizeof(999)}')
print(f'None: {sys.getsizeof(None)}')


# Часть 2
print('----------------------------------')
lst = []
size = sys.getsizeof(lst)
print(f'size: {size}, len: {len(lst)}')
for i in range(100):
    lst.append(i)
    if sys.getsizeof(lst) != size:
        size = sys.getsizeof(lst)
        print(f'size: {size}, len: {len(lst)}')


# Часть 3
print('----------------------------------')
tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(current / 1024, peak / 1024)

tracemalloc.start()
numbers = range(100_000)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(current / 1024, peak / 1024)


