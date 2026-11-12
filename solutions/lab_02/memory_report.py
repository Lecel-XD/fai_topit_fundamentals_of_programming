import sys
import tracemalloc


def measure_part1():
    return {
        'empty list': sys.getsizeof([]),
        'list (len=10)': sys.getsizeof(list(range(1, 11))),
        'tuple': sys.getsizeof(tuple(range(1, 11))),
        'str (len=10)': sys.getsizeof('abcdefghij'),
        'int': sys.getsizeof(999),
        'None': sys.getsizeof(None),
    }


def measure_part2():
    results = []
    lst = []
    size = sys.getsizeof(lst)
    results.append((size, len(lst)))

    for i in range(100):
        lst.append(i)
        new_size = sys.getsizeof(lst)
        if new_size != size:
            size = new_size
            results.append((size, len(lst)))

    return results


def measure_part3():
    results = []

    tracemalloc.start()
    numbers = list(range(100_000))
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results.append(('list(range(100_000))', current / 1024, peak / 1024))

    tracemalloc.start()
    numbers = range(100_000)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results.append(('range(100_000)', current / 1024, peak / 1024))

    return results


def format(header, data1=None, data2=None, data3=None):
    print('----------------------------------')
    print(header)
    print('----------------------------------')

    if data1 is not None:
        if isinstance(data1, dict):
            for name, size in data1.items():
                print(f'{name}: {size}')
        else:
            print(data1)

    if data2 is not None:
        if isinstance(data2, list):
            for size, length in data2:
                print(f'size: {size}, len: {length}')
        else:
            print(data2)
            print('NOOO')

    if data3 is not None:
        if isinstance(data3, list):
            for name, current, peak in data3:
                print(f'{name}: current={current:.2f} KB, peak={peak:.2f} KB')
        else:
            print(data3)
            print('NOOO')

def main():
    data1 = measure_part1()
    data2 = measure_part2()
    data3 = measure_part3()
    format('Часть 1. Размер отдельных объектов', data1=data1)
    format('Часть 2. Рост списка', data1=data2)
    format('Часть 3. Измерение через tracemalloc', data1=data3)


if __name__ == '__main__':
    main()