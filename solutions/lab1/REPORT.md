# **Лабораторная работа 1** 

# **Цель работы**
Разобраться, как CPython выполняет программу, научиться отличать имя от объекта, корректно применять операции сравнения и работать с базовыми типами данных Python.

# **Задачи работы**
научиться:
1) запускать Python-код в REPL и из .py-файла;
2) объяснять путь программы от исходного текста до выполнения байткода;
3) различать выражения и инструкции;
4) объяснять связывание имен с объектами;
5) использовать type(), id(), == и is по назначению;
6) работать с int, float, bool, complex, str и None;
7) выполнять явные преобразования типов;
8) объяснять погрешность вычислений с числами с плавающей точкой;
9) применять индексацию, срезы, Unicode и форматирование строк.

# **Ход работы**

# **Задание 1**

## **Часть 1. Режимы запуска**

В REPL результат сразу выводится на экран, поскольку он предназначен для интерактивной работы и автоматически показывает результат вычислений. При запуске программы из файла арифметическое выражение без команды `print()` вычисляется, но его результат автоматически не выводится на экран. Для вывода результата в файле нужно применить команду `print()`.

### Выполнение выражения в REPL

```text
C:\Users\Иван\Documents\lab_01>python
Python 3.13.14
>>> 2 + 3 * 4
14
```

### Код программы в файле `task_1.py`

```python
print(2 + 3 * 4)
```

### Результат выполнения программы из файла

```text
C:\Users\Иван\Documents\lab_01>python task_1.py
14
```

## **Часть 2** 
1) выражениями являются: "Python", 4 * 2, f"{course}: {hours} часов"
2) инструкциями являются: course = "Python", hours = 4 * 2, print(f"{course}: {hours} часов")
3) литералы: "Python", 4, 2
4) имена: course, hours

## **Часть 3**

### Результат `python --version`

```text
C:\Users\Иван\Documents\lab_01>python --version
Python 3.13.14
```

### Результат `python -m ast task_1.py`

```text
C:\Users\Иван\Documents\lab_01>python -m ast task_1.py
Module(
  body=[
    Expr(
      value=Call(
        func=Name(id='print', ctx=Load()),
        args=[
          BinOp(
            left=Constant(value=2),
            op=Add(),
            right=BinOp(
              left=Constant(value=3),
              op=Mult(),
              right=Constant(value=4)))])),
    Assign(
      targets=[Name(id='course', ctx=Store())],
      value=Constant(value='Python')),
    Assign(
      targets=[Name(id='hours', ctx=Store())],
      value=BinOp(
        left=Constant(value=4),
        op=Mult(),
        right=Constant(value=2)))])
```

### Результат `python -m dis task_1.py`

```text
C:\Users\Иван\Documents\lab_01>python -m dis task_1.py
  0  RESUME                   0

  1  LOAD_NAME                0 (print)
     PUSH_NULL
     LOAD_CONST               0 (14)
     CALL                     1
     POP_TOP

  3  LOAD_CONST               1 ('Python')
     STORE_NAME               1 (course)

  4  LOAD_CONST               2 (4)
     STORE_NAME               2 (hours)
```

Узел, соответствующий присваиванию – Assign, арифметической операции – BinOp, Mult (указание на умножение), вызову `print()` – Call. 
В байткоде за загрузку константы отвечает инструкция `LOAD_CONST`, а за вызов функции – `CALL`.

## Контрольный вопрос
Байткод CPython нельзя считать машинным кодом процессора, поскольку он состоит из инструкций виртуальной машины CPython, а не из инструкций конкретной архитектуры процессора. Для выполнения байткод обрабатывается интерпретатором CPython.


---

# Задание 2

## Часть 1. Прогноз выполнения программы
    print("a == b:", a == b) #прогноз - True
    print("a is b:", a is b) #прогноз - True
    print("a == c:", a == c) #прогноз - True
    print("a is c:", a is c) #прогноз - False
### Фактический результат
    print("a == b:", a == b) #результат - True
    print("a is b:", a is b) #результат - True
    print("a == c:", a == c) #результат - True
    print("a is c:", a is c) #результат - False

## **Часть 2**

1. **Связи имён с объектами**

   ```text
   a ----
         |---> [1000]
   b ----
   c -----> [1000]
   ```

2. **Равенство значений и идентичность объектов**

   Разница между равенством значений и идентичностью объектов заключается в том, что равенство значений определяется путем непосредственного сравнения значений объектов, а идентичность объектов определяется путем сравнения идентификаторов объектов в памяти (например, для `a = [1,2]`, `b = [1,2]` при `a == b` результатом будет `True`, а при `a is b` результатом будет `False`, т.к. это два разных объекта).

3. **Корректная проверка**

   ```python
   c = None
   print(c is None)
   ```

4. **Результат выполнения фрагмента**

   ```text
   True
   True
   ```

   При использовании `==` произошло сравнение значений объектов `first` и `second`, они равны, следовательно, результат команды — `True`.

   При использовании `is` сравнивались идентификаторы объектов в памяти, в данном случае они равны из-за особенностей работы CPython: так как вычисление `"py" + "thon"` происходит на этапе компиляции, CPython использует один и тот же объект строки для обеих переменных `first` и `second`.

## Контрольные вопросы
1.	Нет, инструкция b = a создает имя b, которое ссылается на тот же объект, что и a.
2.	type() возвращает тип данных объекта, id() возвращает идентификатор объекта в памяти.
3.	None сравнивают с помощью is, потому проверяется идентичность с объектом None. Числа и строки сравнивают с помощью ==, потому что необходимо сравнить их значения, а не идентичность объектов.


---

# Задание 3
## Эксперимент А
```python
x = 17
y = 5
print(x + y, type(x + y))
print(x - y, type(x - y))
print(x * y, type(x * y))
print(x / y, type(x / y))
print(x // y, type(x // y))
print(x % y, type(x % y))
print(x ** y, type(x ** y))
```
### Результат
```text
22 <class 'int'>
12 <class 'int'>
85 <class 'int'>
3.4 <class 'float'>
3 <class 'int'>
2 <class 'int'>
1419857 <class 'int'>
```

/ и // возвращают разные значения, потому что / является обычным делением и может возвращать результаты типа float (например, print(17 / 5) -> 3.4, class float), а // - это целочисленное деление с округлением вниз и при делении целых чисел возвращает целое число типа int (например, print(17 // 5) -> 3, class int).

## Эксперимент B

```python
print(2 ** 1000)
```

### Результат

```text
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856
```

Целые числа Python отличаются от целых чисел фиксированной разрядности тем, что тип int не имеет фиксированного количества бит и может хранить целые числа произвольной величины. В языках с фиксированной разрядностью размер и диапазон целых чисел ограничены.

## Эксперимент С
```python
result = 0.1 + 0.2
print(result)
print(result == 0.3)
print(result - 0.3)
print(math.isclose(result, 0.3))
```
### Результат
```text
0.30000000000000004
False
5.551115123125783e-17
True
```

Компьютер хранит float в двоичной системе. Некоторые десятичные дроби нельзя представить в двоичной системе полностью точно, поэтому имеется небольшая погрешность. (Например, при result = 0.1 + 0.2 результатом операции будет 0.30000000000000004). Поэтому числа типа float, полученные при вычислении, не следует напрямую сравнивать при помощи ==. math.isclose() показывает, насколько два числа типа float близки с учетом этой погрешности, его следует использовать для сравнения результатов вычислений типа float.

## Эксперимент D
```python
print(int("42"), type(int("42")))
print(float("3.14"), type(float("3.14")))
print(str(2026), type(str(2026)))
print(bool(0), type(bool(0)))
print(bool(-1), type(bool(-1)))
print(bool(""), type(bool("")))
print(bool("False"), type(bool("False")))
print(complex(2, -3).real, type(complex(2, -3).real))
print(complex(2, -3).imag, type(complex(2, -3).imag))
```

```text
42 <class 'int'>
3.14 <class 'float'>
2026 <class 'str'>
False <class 'bool'>
True <class 'bool'>
False <class 'bool'>
True <class 'bool'>
2.0 <class 'float'>
-3.0 <class 'float'>
```

bool("False") выдает истинное значение, потому что принимает на вход непустую строку. bool выдаст False, если получит на вход пустую строку.

## Контрольные вопросы
1.	Потому что обычное деление в Python всегда возвращает точный ответ, а он может быть дробным. 
2.	int(“42”) преобразует строку в целое число, а int(42.9) преобразует десятичную дробь в целое число, при этом отбрасывая дробную часть, т.е. округляет число в меньшую сторону.
3.	bool(0) и bool(«») являются falsy, т.к. принимают на вход число 0 и пустую строку, а bool выдает ложь при вводе какого-либо пустого значения.


---

# Задание 4
## Код
```python
student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10
symbol = "Я"
print(student.split(" ")[0][0], student.split(" ")[0][-1]) #1
print(student[:4], student[5:]) #2
print(student.upper(), student.lower()) #3
print(student.split(" ")[0][0] + '.' + student.split(" ")[1][0] + '.') #4
print(course[::-1]) #5
print("%s — %s: %i/%i (%1.f.0%%)" % (student, course, completed, total, completed / total * 100)) #6
print("{student} — {course}: {first}/{second} ({res}%)".format(student = student, course = course, first = completed, second = total, res = completed / total * 100))
print(f'{student} — {course}: {completed}/{total} ({completed/total*100}%)')
print(symbol, ord(symbol), chr(ord(symbol)), symbol.encode("utf-8"), len(symbol.encode("utf-8")))
course[0] = 'Я'
print(course)
```
**Фактические результаты:**
```text
А а
Анна Смирнова
АННА СМИРНОВА анна смирнова
А.С.
nohtyP ан яинавориммаргорп ывонсО
Анна Смирнова — Основы программирования на Python: 7/10 (70.0%)
Анна Смирнова — Основы программирования на Python: 7/10 (70.0%)
Анна Смирнова — Основы программирования на Python: 7/10 (70.0%)
Я 1071 Я b'\xd0\xaf' 2
```

Ошибка при изменении первого символа строки присваиванием по индексу: 'str' object does not support item assignment. Причина ошибки заключается в том, что строки в Python являются неизменяемыми. Чтобы изменить символ, можно создать новую строку, например course = ‘Я’ + course[1:].
## Контрольные вопросы
1.	Потому что len(symbol) выводит количество символов в строке, а len(symbol.encode("utf-8")) – количество байтов, необходимых для представления строки в кодировке UTF-8.
2.	В записи text[start:stop:step] start означает левую границу среза, stop — правую границу среза, при этом символ с индексом stop не включается в срез, а step означает шаг, через который выбираются символы. Например, для строки Ivan срез Ivan[0:2] будет равен Iv, а 	для строки Python срез Python[0:4:2] будет равен Pt.
3.	Строка считается неизменяемым объектом, потому что ее непосредственно нельзя изменить после создания. Методы вроде upper() сначала создают новую строку, а уже затем ее изменяют. 


---

# Задание 5
## Код
```python
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
```
### Фактический результат
```text
Enter your name: Иван
Enter your experiment name: Проверка эксперимента
Enter your starts count: 5
Enter your start duration: 1.3
Enter real part: 3
Enter imaginary part: 4
========================================
ЭКСПЕРИМЕНТ: Проверка эксперимента
Исследователь: Иван
Запуски: 5
Общее время: 6.50 с (0.11 мин)
Коэффициент: (3+4j)
Квадрат модуля: 25.00
Есть выполненные запуски: True
Типы данных: username=str, exp_name=str, starts_count=int, start_duration=float, complex_real=float, complex_imag=float
```

1. **Типы объектов, связанные с именами программы**

   username - str  
   exp_name - str  
   starts_count - int  
   start_duration - float  
   complex_real - float  
   complex_imag - float  
   seconds_duration - float  
   minutes_duration - float  
   complex_coefficient - complex  
   complex_square - float  
   has_runs - bool

2. **Разбор арифметической строки**

   Рассмотрим строку:

   `seconds_duration = starts_count * start_duration`

   Имена: seconds_duration, starts_count, start_duration.

   Оператор присваивания: =.

   Арифметический оператор: * (умножение).

   Литералы: отсутствуют.

   Вызовы функций: отсутствуют.

3. **Путь выполнения программы**

   Программа начинается с исходного файла task_5.py, далее Python проверяет синтаксис исходного текста программы и формирует AST-дерево. AST представляет программу в виде узлов: выражений, присваиваний, операторов и т.д. Далее программа компилируется в байткод Python, он компилируется вирт.машиной CPython и ей выполняется (создаются объекты, выполняются операции программы).

4. **Почему результат input() необходимо преобразовывать**

   Функция input() возвращает в качестве результата строку, поэтому его необходимо явно преобразовывать перед арифметическими вычислениями, т.к., например, ‘5’ * 5 не равно 5 * 5.

## Контрольный вопрос
После присваивания нового значения имя связывается с новым объектом, а связь со старым объектом прекращается.

Неожиданности Python:
1. Операции == и is - не одно и то же.
2. Возможность использования разных способов форматирования: .format, f-строки, оператор %
3. Числа с плавающей точкой и их представление в Python (0.3000004 например)
