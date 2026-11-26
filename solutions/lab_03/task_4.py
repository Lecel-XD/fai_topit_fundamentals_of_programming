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