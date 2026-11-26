levels = ['отличный', 'хороший', 'удовлетворительный', 'недостаточный']


def get_mark(score, work_type, skipped):
    '''Вычисляет оценку по заданным данным'''
    if not (0 <= score <= 100):
        return None, f'Некорректное количество баллов: {score}'
    elif not (0 <= skipped <= 5):
        return None, f'Некорректное количество пропусков: {skipped}'
    else:
        if score >= 90:
            idx = 0
        elif score >= 75:
            idx = 1
        elif score >= 60:
            idx = 2
        else:
            idx = 3

        if (idx < 3) and (skipped > 3):
            idx += 1
        match work_type:
            case 'exam':
                description = 'экзаменационная работа'
            case 'project':
                description = 'проектная работа'
            case 'practice':
                description = 'практическая работа'
            case _:
                description = 'неизвестный'
    return levels[idx], description


def main():
    '''Для каждого студента вычисляет результат работы и её тип'''
    students = {
        'Имя_1': (0, 'exam', 4),
        'Имя_2': (59, 'project', 1),
        'Имя_3': (-20, 'practice', 0),
        'Имя_4': (80, 'project', 3),
        'Имя_5': (75, 'practice', 4),
        'Имя_6': (89, 'exam', 1),
        'Имя_7': (90, 'practice', 2),
        'Имя_8': (100, 'exam', 5),
        'Имя_9': (74, 'exam', 0),
        'Имя_10': (60, 'something', 3),
        'Имя_11': (74, 'exam', -3),
        'Имя_12': (89, 'something', -4)
    }
    results = {}
    for name, info in students.items():
        mark, descr = get_mark(*info)
        if mark is None:
            print(f'{name}: {descr}')
            continue
        results[mark] = results.get(mark, 0) + 1
        print(f'{name}. Тип: {descr}, результат: {mark}')
    print('-------------')
    for i in levels:
        print(f'{i}: {results.get(i, 0)}')


if __name__ == '__main__':
    main()

