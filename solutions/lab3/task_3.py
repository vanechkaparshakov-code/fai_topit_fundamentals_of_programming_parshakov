
#данные о студентах
submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = set([x[0] for x in submissions]) #множество всех студентов
works = set(x[1] for x in submissions) #множество всех работ
student_attempts = {}
best_attempts = {}
count_attempts = {}
# print(students, works)

for x in submissions:
    if x[0] not in student_attempts:
        student_attempts[x[0]] = []
    student_attempts[x[0]] += [x[1:]]
# print(student_attempts) #составляем словарь студент: попытки

for y in submissions:
    if y[:2] not in best_attempts:
        best_attempts[y[:2]] = 0
        if y[-1] > best_attempts[y[:2]]:
            best_attempts[y[:2]] = y[-1]
# print(best_attempts) #составляем словарь (студент, лабораторная): лучшая попытка

for z in submissions:
    if z[:2] not in count_attempts:
        count_attempts[z[:2]] = 0
    count_attempts[z[:2]] += 1
# print(count_attempts) #составляем словарь (студент, лабораторная): количество попыток

first_work = set([x[0] for x in submissions if x[1] == 'lab_01']) #множество студентов, сдавших первую работу
second_work = set([x[0] for x in submissions if x[1] == 'lab_02'])  #множество студентов, сдавших вторую работу
all_works = first_work & second_work
print(all_works) #множество студентов, сдавших обе работы

#изменяем все структуры без полного их обновления после добавления записи в sumbissions
submissions.append(("daria", "lab_02", 5))

students.add(submissions[-1][0])
works.add(submissions[-1][1])

if submissions[-1][0] not in student_attempts:
    student_attempts[submissions[-1][0]] = 0
student_attempts[submissions[-1][0]] += submissions[-1][1:]

if submissions[-1][:2] not in best_attempts:
    best_attempts[submissions[-1][:2]] = 0
if submissions[-1][-1] > best_attempts[submissions[-1][:2]]:
    best_attempts[submissions[-1][:2]] = submissions[-1][-1]

if submissions[-1][:2] not in count_attempts:
    count_attempts[submissions[-1][:2]] = 0
count_attempts[submissions[-1][:2]] += 1

print(students, works, student_attempts, best_attempts, count_attempts, sep='\n')

#обработка текстового запроса через match/case, обработка неподходящего ключа через case _, обработка отсутствия нужного ключа в словаре через try except keyerror
request = input().split()

try:
    match request[0]:
        case 'student':
            print(student_attempts[request[-1]])
        case 'best':
            print(best_attempts[*request[1:]])
        case 'attempts':
            print(count_attempts[*request[1:]])
        case 'completed':
            if request[-1] == 'lab_01':
                print(first_work)
            elif request[-1] == 'lab_02':
                print(second_work)
        case _:
            print('Нет подходящего ключа.')
except KeyError:
    print('Отсутствует требуемый ключ')


