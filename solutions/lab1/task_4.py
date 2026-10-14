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
print(symbol, ord(symbol), chr(ord(symbol)), symbol.encode("utf-8"), len(symbol.encode("utf-8"))) #7
# course[0] = 'Я' #8
# print(course)
