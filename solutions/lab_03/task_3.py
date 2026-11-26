students = set()
labs = set()
attempts = {}
best_results = {}
counts = {}


def get_info(command, *args):
    """Возвращает информацию по команде"""
    match command:
        case 'student':
            if len(args) != 1:
                return 'Использование: student <name>.'
            name = args[0]
            if name in students:
                return f'{name} является студентом.'
            return f'Студент {name} не найден.'
        case 'best':
            if len(args) != 2:
                return 'Использование: best <name> <lab>'
            key = (args[0], args[1])
            if key not in best_results:
                return f'Нет данных для {key}'
            return f'Лучший результат у {key[0]} (работа {key[1]}): {best_results[key]}'
        case 'attempts':
            if len(args) != 2:
                return 'Использование: attempts <name> <lab>'
            key = (args[0], args[1])
            return f'Количество попыток для {key[0]} (работа {key[1]}): {counts.get(key, 0)}'
        case 'completed':
            if len(args) != 1:
                return 'Использование: completed <lab>.'
            lab = args[0]
            if lab in labs:
                return f'{lab} есть в списке сданных лабораторных.'
            return f'Никто не сдал {lab}...'
        case _:
            return f'Неизвестная команда: {command}'



def add_submission(person):
    """Добавляет данные о пользователе"""
    name, lab, score = person
    students.add(name)
    labs.add(lab)
    attempts.setdefault(name, []).append((lab, score))
    key = (name, lab)
    if key not in best_results or score > best_results[key]:
        best_results[key] = score
    counts[key] = counts.get(key, 0) + 1


def print_info():
    """Печатает общую аналитику"""
    print(f'Студенты: {students}')
    print(f'Сданные лабы: {labs}')
    print(f'Список попыток студентов: {attempts}')
    print(f'Лучшие результаты: {best_results}')
    print(f'Количество попыток на лабу: {counts}', end='\n\n')


def main():
    submissions = [
        ("anna", "lab_01", 5),
        ("boris", "lab_01", 4),
        ("anna", "lab_02", 5),
        ("daria", "lab_01", 3),
        ("boris", "lab_02", 5),
        ("anna", "lab_01", 4)
    ]

    for person in submissions:
        add_submission(person)

    print('До добавления:')
    print_info()

    newbie = ("valeria", "lab_02", 5)
    submissions.append(newbie)
    add_submission(newbie)

    print('После добавления:')
    print_info()

    lab_01 = {name for (name, lab) in best_results if lab == 'lab_01'}
    lab_02 = {name for (name, lab) in best_results if lab == 'lab_02'}
    both = lab_01 & lab_02
    print('Сдали обе лабы:', both)

    requests = ['student anna', 'best anna lab_01','attempts boris lab_02', 'completed lab_01']
    for request in requests:
        print(get_info(*request.strip().split()))


if __name__ == '__main__':
    main()
