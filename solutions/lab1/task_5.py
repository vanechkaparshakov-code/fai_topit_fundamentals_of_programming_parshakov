"""Программа для расчёта параметров эксперимента и его длительности."""
username = input("Enter your name: ")
exp_name = input("Enter your experiment name: ")
starts_count = int(input("Enter your starts count: "))
start_duration = float(input("Enter your start duration: "))
complex_real = float(input("Enter real part: "))
complex_imag = float(input("Enter imaginary part: "))
seconds_duration = starts_count * start_duration
minutes_duration = seconds_duration / 60
complex_coefficient = complex(complex_real, complex_imag)
complex_square = complex_real ** 2 + complex_imag ** 2
has_runs = bool(starts_count)
print('========================================')
print(f'ЭКСПЕРИМЕНТ: {exp_name}')
print(f'Исследователь: {username}')
print(f'Запуски: {starts_count}')
print(f'Общее время: {seconds_duration:.2f} с ({minutes_duration:.2f} мин)')
print(f'Коэффициент: {complex_coefficient}')
print(f'Квадрат модуля: {complex_square:.2f}')
print(f'Есть выполненные запуски: {has_runs}')

print(
    f'Типы данных: username={type(username).__name__}, '
    f'exp_name={type(exp_name).__name__}, '
    f'starts_count={type(starts_count).__name__}, '
    f'start_duration={type(start_duration).__name__}, '
    f'complex_real={type(complex_real).__name__}, '
    f'complex_imag={type(complex_imag).__name__}'
)