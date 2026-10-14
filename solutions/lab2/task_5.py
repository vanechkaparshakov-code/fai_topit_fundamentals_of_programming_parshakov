import sys

#Часть 1. Размер отдельных объектов

empty_array = []
ten_array = [0,1,2,3,4,5,6,7,8,9]
ten_tuple = tuple(ten_array)
ten_string = '0123456789'
number = 0
obj = None
print('Пустой список:', sys.getsizeof(empty_array))
print('Список из 10 целых чисел:', sys.getsizeof(ten_array))
print('Кортеж из 10 целых чисел:', sys.getsizeof(ten_tuple))
print('Строка из 10 символов:', sys.getsizeof(ten_string))
print('Целое число:', sys.getsizeof(number))
print('None:', sys.getsizeof(obj))

#Часть 2. Рост списка

arr = []
start_size = sys.getsizeof(arr)
for i in range(100):
    arr.append(0)
    new_size = sys.getsizeof(arr)
    if new_size != start_size:
        print(len(arr), new_size)
        start_size = new_size

#Часть 3. Измерение через tracemalloc
import tracemalloc

#list
tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
print(f"Текущая память: {current / 1024:.2f} КБ")
print(f"Пиковая память: {peak / 1024:.2f} КБ")
tracemalloc.stop()

#range
tracemalloc.start()
numbers_1 = range(100_000)
current, peak = tracemalloc.get_traced_memory()
print(f"Текущая память: {current / 1024:.2f} КБ")
print(f"Пиковая память: {peak / 1024:.2f} КБ")
tracemalloc.stop()
