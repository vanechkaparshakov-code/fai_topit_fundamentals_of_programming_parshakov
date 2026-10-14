a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

#1
second = [10, 20, 30]
print(id(first), id(second))

#2
print(first == second, first is second)

#3
second.append(40)
print(first,second)

from copy import *
#Практическая задача
config_1 = {
    'name': 'project1',
    'members': ['Иван', 'Пётр'],
    'parameters': ['first', 'top_it']
}

config_2 = config_1
print(id(config_2), id(config_1))
config_2['members'].append('Катя')
print('Нежелательное совместное изменение: ')
print('Конфигурация 1:', config_1['members'])
print('Конфигурация 2:', config_2['members'])

config_2 = deepcopy(config_1)
config_2['members'].append('Паша')
print('После изменения независимой конфигурации: ')
print('Конфигурация 1:', config_1['members'])
print('Конфигурация 2:', config_2['members'])

assert config_1 is not config_2
assert config_1['members'] is not config_2['members']
assert config_1['parameters'] is not config_2['parameters']
print('Конфигурации независимы')
