students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

CATEGORIES = ["отличный", "хороший", "удовлетворительный", "недостаточный", "нет данных"]


def mean(values):
    """Считает среднее арифметическое"""
    if not values:
        return None
    summa = 0
    for value in values:
        summa += value
    return summa / len(values)


def minimum(values):
    """Ищет минимальный элемент без использования min()."""
    if not values:
        return None
    mn = values[0]
    for value in values[1:]:
        if value < mn:
            mn = value
    return mn


def maximum(values):
    """Ищет максимальный элемент без использования max()."""
    if not values:
        return None
    mx = values[0]
    for value in values[1:]:
        if value > mx:
            mx = value
    return mx


def classify(score):
    """Возвращает текстовую категорию результата"""
    if score is None:
        return CATEGORIES[4]
    if score >= 90:
        return CATEGORIES[0]
    if score >= 75:
        return CATEGORIES[1]
    if score >= 60:
        return CATEGORIES[2]
    return CATEGORIES[3]


def student_summary(name, results):
    """Возвращает словарь с итогами одного студента."""
    avg = mean(results)
    return {
        "name": name,
        "results": list(results),
        "mean": avg,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(avg),
        "count": len(results),
    }


def group_summary(students):
    """Возвращает общую статистику группы."""
    summaries = [student_summary(name, res) for name, res in students.items()]
    means = [s["mean"] for s in summaries if s["mean"] is not None]

    group_avg = None
    if means:
        group_sum = 0
        for m in means:
            group_sum += m
        group_avg = group_sum / len(means)

    category_counts = {c: 0 for c in CATEGORIES}
    for s in summaries:
        category_counts[s["category"]] += 1

    return {
        "students": summaries,
        "group_mean": group_avg,
        "category_counts": category_counts,
        "total_students": len(summaries),
    }


def find_top_students(students):
    """Список студентов с наибольшим средним."""
    summaries = [student_summary(name, res) for name, res in students.items()]
    best = None
    persons = []
    for person in summaries:
        cur_av = person['mean']
        if cur_av is not None:
            if best is None or cur_av > best:
                persons = [person['name']]
                best = cur_av
            elif cur_av == best:
                persons.append(person['name'])
    return persons


def format_report(student_data, group_data, top_names=None):
    """Печатает итоговый отчёт. Входные данные не изменяются."""
    print("=== Результаты студентов ===")
    for s in student_data:
        if s["mean"] is None:
            print(f'{s["name"]}: нет данных (попыток: {s["count"]})')
        else:
            print(f'{s["name"]}: среднее {s["mean"]:.2f}, мин {s["min"]}, макс {s["max"]}, категория: {s["category"]}')

    print()
    print("=== Статистика группы ===")
    gr_av = group_data["group_mean"]
    print(f'Всего студентов: {group_data["total_students"]}')
    print(f'Средний результат группы: {"нет данных" if gr_av is None else f"{gr_av:.2f}"}')
    print("По категориям:")
    for category, cnt in group_data["category_counts"].items():
        print(f'  {category}: {cnt}')

    if top_names is None:
        top_names = [s["name"] for s in student_data
                     if s["mean"] is not None and s["mean"] == max(
                         (x["mean"] for x in student_data if x["mean"] is not None),
                         default=None)]
    print(f'Лидер(ы): {", ".join(top_names) if top_names else "нет"}')


def test_contracts():
    """Проверка контрактов отдельных функций."""

    assert mean([10, 20, 30]) == 20.0
    assert mean([]) is None
    assert mean([5]) == 5.0

    assert minimum([3, 1, 4, 1, 5]) == 1
    assert maximum([3, 1, 4, 1, 5]) == 5
    assert minimum([]) is None
    assert maximum([]) is None
    assert minimum([42]) == 42
    assert maximum([42]) == 42

    assert classify(95) == "отличный"
    assert classify(90) == "отличный"
    assert classify(89) == "хороший"
    assert classify(75) == "хороший"
    assert classify(74) == "удовлетворительный"
    assert classify(60) == "удовлетворительный"
    assert classify(59) == "недостаточный"
    assert classify(0) == "недостаточный"
    assert classify(None) == "нет данных"

    s = student_summary("Тест", [])
    assert s["mean"] is None
    assert s["min"] is None
    assert s["max"] is None
    assert s["category"] == "нет данных"
    assert s["count"] == 0

    assert find_top_students({}) == []
    assert find_top_students({"A": []}) == []
    assert find_top_students({"A": [80, 90], "B": [80, 90]}) == ["A", "B"]
    assert find_top_students({"A": [100], "B": [50]}) == ["A"]


def main():
    test_contracts()

    data = group_summary(students)
    format_report(data["students"], data)


if __name__ == "__main__":
    main()