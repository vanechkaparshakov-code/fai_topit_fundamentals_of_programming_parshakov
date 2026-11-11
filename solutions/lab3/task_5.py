
students_0 = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

students_1 = {
    "Анна": [78, 91, 84, 88]
}

students_2 = {
    "Анна": [78, 91, 84, 88],
    "Борис": [78, 91, 84, 88],
    "Даниил": [78, 91, 84, 88]
}

students_3 = {}

students_4 = {
    "Анна": [78, 91, 84, 88],
    "Борис": [78, 1, 4, 88],
    "Даниил": []
}

students_5 = {
    "Анна": [90,90,88,92],
    "Борис": [74,76,74,76]
}

def mean(values):
    if not isinstance(values, list) or not values:
        return None
    return sum(values) / len(values)


def minimum(values):
    if not isinstance(values, list) or not values:
        return None
    min_num = values[0]
    for num in values:
        if num < min_num:
            min_num = num
    return min_num


def maximum(values):
    if not isinstance(values, list) or not values:
        return None
    max_num = values[0]
    for num in values:
        if num > max_num:
            max_num = num
    return max_num


def classify(score):
    if score is None:
        return "нет данных"
    if score < 60:
        return "недостаточный"
    elif score < 75:
        return "удовлетворительный"
    elif score < 90:
        return "хороший"
    return "отличный"


def student_summary(name, results):
    avg = mean(results)
    return {
        "name": name,
        "mean": avg,
        "minimum": minimum(results),
        "maximum": maximum(results),
        "category": classify(avg)
    }


def group_summary(students):
    categories = {
        "недостаточный": 0,
        "удовлетворительный": 0,
        "хороший": 0,
        "отличный": 0,
        "нет данных": 0
    }

    students_sum = 0
    count_points = 0

    for results in students.values():
        avg = mean(results)
        category = classify(avg)

        categories[category] += 1

        if results:
            students_sum += sum(results)
            count_points += len(results)

    if count_points == 0:
        mean_group = None
    else:
        mean_group = students_sum / count_points

    return {
        "categories": categories,
        "mean_group": mean_group,
        "number_of_students": len(students)
    }


def find_top_students(students):
    stats = []

    for name, results in students.items():
        avg = mean(results)

        if avg is not None:
            stats.append((name, avg))

    if not stats:
        return []

    max_value = maximum([x[1] for x in stats])
    top_students = [(name, score) for name, score in stats if score == max_value]

    return top_students


def format_report(student_data, group_data):
    report = "ОТЧЁТ ПО РЕЗУЛЬТАТАМ ГРУППЫ\n\n"

    report += "СТАТИСТИКА СТУДЕНТОВ:\n"

    for name, stats in student_data.items():
        report += f"\n{name}:\n"

        if stats["mean"] is None:
            report += "Результаты отсутствуют\n"
            report += f"Категория: {stats['category']}\n"
            continue

        report += f"Средний балл: {stats['mean']:.2f}\n"
        report += f"Минимальный балл: {stats['minimum']}\n"
        report += f"Максимальный балл: {stats['maximum']}\n"
        report += f"Категория: {stats['category']}\n"

    report += "\nОБЩАЯ СТАТИСТИКА ГРУППЫ:\n"

    report += (
        f"Количество студентов: "
        f"{group_data['number_of_students']}\n"
    )

    if group_data["mean_group"] is not None:
        report += (
            f"Средний результат группы: "
            f"{group_data['mean_group']:.2f}\n"
        )
    else:
        report += "Средний результат группы: нет данных\n"

    report += "\nКОЛИЧЕСТВО СТУДЕНТОВ ПО КАТЕГОРИЯМ:\n"

    for category, count in group_data["categories"].items():
        report += f"{category}: {count}\n"

    report += "\nЛИДЕРЫ ГРУППЫ:\n"

    top_students = find_top_students(students_5)

    if not top_students:
        report += "Нет данных\n"
    else:
        for name, score in top_students:
            report += f"{name} — {score:.2f}\n"

    report += "\nРЕЙТИНГ ГРУППЫ:\n"

    rating = sorted(
        student_data.items(),
        key=lambda x: (
            x[1]["mean"] is not None,
            x[1]["mean"] if x[1]["mean"] is not None else 0
        ),
        reverse=True
    )

    for place, (name, stats) in enumerate(rating, 1):
        if stats["mean"] is not None:
            report += f"{place}. {name} — {stats['mean']:.2f}\n"
        else:
            report += f"{place}. {name} — нет данных\n"

    return report


student_data = {}

for name, results in students_5.items():
    student_data[name] = student_summary(name, results)

group_data = group_summary(students_5)

print(format_report(student_data, group_data))









