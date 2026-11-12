def arithmetic_mean(values: list[float]) -> float:
    if not isinstance(values, list) or not values or not all(isinstance(x, (int, float)) for x in values):
        return None
    summ = sum(values)
    length = len(values)
    return summ / length

def normalize_name(name: str) -> str:
    if not isinstance(name, str):
        return None
    result = " ".join(name.split()).title().replace(' ', '')
    return result

def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    if not isinstance(student, str) or not isinstance(results, list) or not results or not all(isinstance(x, int) for x in results):
        return None
    if not isinstance(precision, int) or precision < 0:
        return None
    if not isinstance(prefix, str):
        return None
    average_p = sum(results) / len(results)
    return f'{prefix} студента {student}: {average_p:.{precision}f}'

def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    if not(all(isinstance(x, str) for x in tags)):
        return None
    res = set(tags)
    if lowercase:
        return tuple([x.lower() for x in res])
    else:
        return tuple(res)

assert arithmetic_mean([2, 4, 6]) == 4
assert arithmetic_mean([1, 2, 3, 4]) == 2.5
assert arithmetic_mean([]) is None

assert normalize_name("ivan ivanov") == "IvanIvanov"
assert normalize_name("  alex   SMITH  ") == "AlexSmith"
assert normalize_name(123) is None

assert build_report("Иван", [4, 5, 5]) == "Результат студента Иван: 4.67"
assert build_report("Анна", [3, 4], precision=1) == "Результат студента Анна: 3.5"
assert build_report("Иван", ["5", 4]) is None

assert set(collect_tags("Python", "Java")) == {"python", "java"}
assert set(collect_tags("Python", "Java", lowercase=False)) == {"Python", "Java"}
assert collect_tags() == ()


print(arithmetic_mean([2, 4, 6]))
print(arithmetic_mean(values=[2, 4, 6]))

print(normalize_name("ivan ivanov"))
print(normalize_name(name="ivan ivanov"))

print(build_report("Иван", [4, 5, 5]))
print(build_report(
    student="Иван",
    results=[4, 5, 5],
    precision=1,
    prefix="Оценка"
))

print(collect_tags("Python", "Java"))
print(collect_tags("Python", "Java", lowercase=False))


numbers = [2, 4, 6]
print(arithmetic_mean(*[numbers]))

report_data = ["Иван", [4, 5, 5]]
print(build_report(*report_data))

report_options = {
    "student": "Анна",
    "results": [4, 5, 5],
    "precision": 1,
    "prefix": "Оценка"
}
print(build_report(**report_options))

course = "Python"

def outer():
    course = "Основы программирования"

    def inner():
        nonlocal course
        course = "Алгоритмы"

    inner()
    print(course)

outer()
print(course)


def add_result(value, results=[]):
    results.append(value)
    return results


def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results
print(add_result('fsfsf'))
print(add_result('2f'))


def operation(x):
    return x**2
def apply_to_results(operation, values):
    return [operation(x) for x in values]
print(apply_to_results(operation, [2,3,4]))
print(apply_to_results(lambda x: x*3, [2,3,4]))

def make_threshold_checker(threshold):
    def check(value):
        return value > threshold
    return check
check_10 = make_threshold_checker(10)
check_50 = make_threshold_checker(50)
print(check_10(20))
print(check_50(20))
