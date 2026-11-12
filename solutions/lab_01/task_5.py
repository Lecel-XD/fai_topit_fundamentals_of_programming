"""Программа для создания информационной карточки вычислительного эксперимента"""
researcher_name = input("Введите имя исследователя: ")
experiment_name = input("Название эксперимента: ")
launch_count = int(input("Количество запусков: "))
launch_duration = float(input("Длительность одного запуска: "))
real_factor, image_factor = float(input("Действительная часть комплексного коэффициента: ")), float(input("Мнимая часть комплексного коэффициента: "))


total_duration = launch_count * launch_duration
complex_factor = complex(real_factor, image_factor)
square_complex = real_factor ** 2 + image_factor ** 2
has_runs = bool(launch_count)


print('========================================')
print(f'ЭКСПЕРИМЕНТ: {experiment_name}')
print(f'Исследователь: {researcher_name}')
print(f'Запуски: {launch_count}')
print(f'Общее время: {total_duration:.2f} с ({(total_duration / 60):.2f} мин)')
print(f'Коэффициент: {complex_factor}')
print(f'Квадрат модуля: {square_complex:.2f}')
print(f'Есть выполненные запуски: {has_runs}')
print('========================================', end='\n\n\n')


print(f'Типы значений. researcher_name: {type(researcher_name)}, \
experiment_name: {type(experiment_name)}, launch_count: {type(launch_count)}, \
launch_duration: {type(launch_duration)}, real_factor: {type(real_factor)}, image_factor: {type(image_factor)}.')

