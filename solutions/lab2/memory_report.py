import sys
import tracemalloc

res_1 = []
res_2 = []
res_3 = []
res_4 = []
res_5 = []

part_1 = {
    'empty_array': [],
    'ten_array': [0,1,2,3,4,5,6,7,8,9],
    'ten_tuple': tuple([0,1,2,3,4,5,6,7,8,9]),
    'ten_string': '0123456789',
    'number': 0,
    'obj':  None
}

#сценарий 1
for i in part_1.values():
    try:
        if isinstance(i, int):
            res_1.append(f'{i}: Число элементов - {len(str(i))}, размер внешнего объекта - {sys.getsizeof(i)}')
        else:
            res_1.append(f'{i}: Число элементов - {len(i)}, размер внешнего объекта - {sys.getsizeof(i)}')
    except:
        res_1.append(f'{i}: Число элементов - 0, размер внешнего объекта - {sys.getsizeof(i)}')

#сценарий 2
arr = []
start_size = sys.getsizeof(arr)
for i in range(100):
    arr.append(0)
    new_size = sys.getsizeof(arr)
    if new_size != start_size:
        res_2.append(f'Список из нулей: Число элементов - {len(arr)}, размер внешнего объекта - {new_size}')
        start_size = new_size

#сценарий 3
tracemalloc.start()
numbers = list(range(100_000))
current_1, peak_1 = tracemalloc.get_traced_memory()
res_3.append(f'Список из 100000 чисел: Число элементов - {len(numbers)}, Размер внешнего объекта - {sys.getsizeof(numbers)}, Текущий объем выделенной памяти - {current_1 / 1024:.2f} КБ, Пиковый объем выделенной памяти - {peak_1 / 1024:.2f} КБ ')
tracemalloc.stop()

#сценарий 4
tracemalloc.start()
numbers_1 = range(100_000)
current_2, peak_2 = tracemalloc.get_traced_memory()
res_4.append(f'Список из 100000 чисел: Число элементов - {len(numbers)}, Размер внешнего объекта - {sys.getsizeof(numbers)}, Текущий объем выделенной памяти - {current_2 / 1024:.2f} КБ, Пиковый объем выделенной памяти - {peak_2 / 1024:.2f} КБ ')
tracemalloc.stop()

#сценарий 5
res_5.append(f'Отношение пикового объема двух сравниваемых сценариев: {peak_2 / peak_1}')

print('СЦЕНАРИЙ 1. РАЗМЕР ОТДЕЛЬНЫХ ОБЪЕКТОВ')
print('_____________________________________')
for _ in range(len(res_1)):
    print(res_1[_])
print('_____________________________________')
print('СЦЕНАРИЙ 2. РОСТ СПИСКА')
print('_____________________________________')
for _ in range(len(res_2)):
    print(res_2[_])
print('_____________________________________')
print('СЦЕНАРИЙ 3. ИЗМЕРЕНИЕ ЧЕРЕЗ TRACEMALLOC, СПИСОК')
print('_____________________________________')
for _ in range(len(res_3)):
    print(res_3[_])
print('_____________________________________')
print('СЦЕНАРИЙ 4. ИЗМЕРЕНИЕ ЧЕРЕЗ TRACEMALLOC, RANGE')
print('_____________________________________')
for _ in range(len(res_4)):
    print(res_4[_])
print('_____________________________________')
print(*res_5)