def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""

    assert isinstance(values, list), 'values должен быть списком'
    if not values:
        return 0.0
    summa = 0
    for el in values:
        summa += el
    return summa / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""

    assert isinstance(name, str), 'name должен быть строкой'
    if not name.strip():
        return ''
    return ' '.join(part.capitalize() for part in name.split())


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""

    assert isinstance(student, str), 'student должен быть строкой'
    assert isinstance(results, list), 'results должен быть списком'
    assert precision >= 0, 'precision не может быть отрицательным'

    name = normalize_name(student)
    if not results:
        return f'{prefix}: {name} - нет данных'
    average = arithmetic_mean(results)
    return f'{prefix}: {name} - среднее {average:.{precision}f}'


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""

    assert all(isinstance(t, str) for t in tags)
    unique = set()
    cleaned_tags = []
    for tag in tags:
        cleaned = tag.strip()
        if not cleaned:
            continue
        if lowercase:
            cleaned = cleaned.lower()
        if cleaned in unique:
            continue
        unique.add(cleaned)
        cleaned_tags.append(cleaned)
    return tuple(cleaned_tags)


def run_tests():
    """Проверки поведения функций"""
    assert arithmetic_mean([1, 2, 3]) == 2.0
    assert arithmetic_mean([5]) == 5.0
    assert arithmetic_mean([]) == 0.0
    assert isinstance(arithmetic_mean([1, 2]), float)
    src = [3, 1, 2]
    arithmetic_mean(src)
    assert src == [3, 1, 2], 'исходный список не должен меняться'

    assert normalize_name('  anna   geiko ') == 'Anna Geiko'
    assert normalize_name('ANNA') == 'Anna'
    assert normalize_name('') == ''
    assert normalize_name('   ') == ''

    assert build_report('Anna', [5, 4], precision=1) == 'Результат: Anna - среднее 4.5'
    assert build_report('Anna', [], prefix='Итог') == 'Итог: Anna - нет данных'
    assert build_report('ANNA', [5], precision=0) == 'Результат: Anna - среднее 5'

    assert collect_tags('Python', 'python', ' PYTHON ') == ('python',)
    assert collect_tags('a', '', 'b') == ('a', 'b')
    assert collect_tags('A', 'B', lowercase=False) == ('A', 'B')
    assert isinstance(collect_tags('x'), tuple)
    assert collect_tags('b', 'a', 'b') == ('b', 'a'), 'порядок первого вхождения'

    print('Все проверки прошли')


# Практическое расширение
def apply_to_results(operation, values):
    """Применяет operation к каждому элементу values, возвращает новый список."""
    return [operation(v) for v in values]


def make_threshold_checker(threshold):
    """Возвращает функцию, проверяющую результат на превышение порога."""
    def check(value):
        return value >= threshold
    return check


def last_part():
    def double(x):
        return x * 2

    values = [3, 5, 7]

    print('Именованная x * 2:', apply_to_results(double, values))
    print('Lambda x + 1:', apply_to_results(lambda x: x + 1, values))
    assert values == [3, 5, 7], 'исходный список не должен меняться'

    is_greater_50 = make_threshold_checker(50)
    is_greater_70 = make_threshold_checker(70)

    print('is_greater_50(75):', is_greater_50(75))
    print('is_greater_50(40):', is_greater_50(40))
    print('is_greater_70(76):', is_greater_70(76))
    print('is_greater_70(65):', is_greater_70(65))

    print('Замыкание is_greater_50:', is_greater_50.__closure__[0].cell_contents)
    print('Замыкание is_greater_70:', is_greater_70.__closure__[0].cell_contents)

    scores = [55, 72, 88, 95]
    print('pass_check по scores:', apply_to_results(is_greater_50, scores))
    print('excellent_check по scores:', apply_to_results(is_greater_70, scores))





def main():
    print(arithmetic_mean([4, 5, 6]))
    print(normalize_name('  IVAN   ivanov '))

    print(build_report('Anna', [5, 4, 3], precision=3, prefix='Средний балл'))
    print(collect_tags('Math', 'math', ' Physics ', lowercase=True))

    tag_list = ['Python', 'python', 'Math']
    print(collect_tags(*tag_list))

    results = [5, 4]
    options = {'precision': 1, 'prefix': 'Итог'}
    print(build_report('Boris', results, **options))

    print(build_report('Anna', []))
    print(collect_tags('', '  ', 'x', 'x'))


if __name__ == '__main__':
    run_tests()
    main()
    last_part()

# Исследование LEGB
course = "Python"

def outer():
    year = 1
    def inner():
        nonlocal year
        year += 1
        return year
    inner()
    inner()
    return year

print(outer())
print(course)


# Ошибка изменяемого значения по умолчанию
def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results

print(add_result(1))
print(add_result(2))


