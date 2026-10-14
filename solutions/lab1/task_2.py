a = 500
b = a
c = int("500")

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b) #прогноз - True
print("a is b:", a is b) #прогноз - True
print("a == c:", a == c) #прогноз - True
print("a is c:", a is c) #прогноз - False

c = None
print('c is None:', c is None)

first = "python"
second = "py" + "thon"

print(first == second)
print(first is second)

