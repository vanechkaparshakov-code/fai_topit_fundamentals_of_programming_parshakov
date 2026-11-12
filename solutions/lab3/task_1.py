#составляем статистику для каждого студента - тип работы и уровень результата

result = int(input('Введите результат студента - целое число от 0 до 100: '))
work_type = input('Укажите тип работы: ')
misses = int(input('Укажите число пропущенных занятий: '))

students = [
    (82, "exam", 4),
    (95, "project", 1),
    (67, "practice", 2),
    (54, "exam", 0),
    (76, "project", 5),
    (91, "practice", 3),
    (73, "exam", 4),
    (88, "project", 0),
    (60, "practice", 1),
    (100, "exam", 5)
]

stats = []

count_levels = {
    'недостаточный': 0,
    'удовлетворительный': 0,
    'хороший': 0,
    'отличный': 0
}

levels = ["недостаточный", "удовлетворительный", "хороший", "отличный"]
points = [0, 60, 75, 90]


for student in students:
    result = student[0]
    work_type = student[1]
    misses = student[2]

    if not(0 <= result <= 100) or not(0 <= misses <= 5): проверка корректности ввода
        print('Введены некорректные значения. Попробуйте заново')
    else:
        level = max(i for i, point in enumerate(points) if result >= point) #максимальный индекс массива points, результат по которому меньше чем результат студента
        if misses > 3:
            level = max(0, level - 1) #снижаем уровень, если много пропусков
        fin_level = levels[level] #итоговый уровень

        match work_type: #через match case определяется тип работы, если введено неожидаемое значение, то срабатывает ветка case _
            case 'exam':
                fin_type = 'Экзаменационная работа'
            case 'project':
                fin_type = 'Проектная работа'
            case 'practice':
                fin_type = 'Практическая работа'
            case _:
                fin_type = 'Неизвестный вид работы'

        total_result = f'Студент {students.index(student) + 1}: {fin_level}; {fin_type}' #статистика для каждого студента
        stats.append(total_result)
        count_levels[fin_level] += 1
        print(total_result)
print(count_levels)
