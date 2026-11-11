measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

summ = 0
min_num = float('+inf')
max_num = float('-inf')
even_num = 0
count_above_average = 0

for num in measurements:
    summ += num #сумма

    if num < min_num: #минимум
        min_num = num

    if num > max_num: #максимум
        max_num = num

    if num % 2 == 0: #чётные
        even_num += 1

average = summ / len(measurements)

for number in measurements:
    if number > average: #превосходит среднее арифметическое
        count_above_average += 1

print(summ, min_num, max_num, even_num, count_above_average)


def line_search(x, arr):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if x == arr[i]:
            return i, comparisons
    return -1, comparisons



def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

print(is_prime(7))

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def binary_search(x, arr, left, right,  comparisons=None):
    if comparisons is None:
        comparisons = [0]

    if right < left:
        return -1, comparisons[0]

    middle = (right  + left) // 2

    comparisons[0] += 1
    if x == arr[middle]:
        return middle, comparisons[0]

    comparisons[0] += 1
    if x < arr[middle]:
        return binary_search(x, arr, left, middle-1, comparisons)

    return binary_search(x, arr, middle+1, right, comparisons)

comparisons = [0]

datasets = {
    10: list(range(1, 11)),
    100: list(range(1, 101)),
    1000: list(range(1, 1001))
}

for item in datasets.values():
    lin_res, lin_comps = line_search(item[-1], item)
    print(f'Линейный поиск: результат - {lin_res}, количество сравнений - {lin_comps}')
    bin_res, bin_comps = binary_search(item[-1], item, 0, len(item)-1,  comparisons)
    print(f'Бинарный поиск: результат - {bin_res}, количество сравнений - {bin_comps}')
    print('_____________________')





