import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print(gc.collect())
print(gc.get_threshold())
print(gc.get_count())

id_first = id(first)
id_second = id(second)

del first
del second

collect = gc.collect()
print(collect)
#
gc.collect()

#эксперимент
gc.disable()
arr_1 = []
arr_2 = []
arr_3 = []
arr_1.append(arr_2)
arr_2.append(arr_3)
arr_3.append(arr_1)


del arr_1
del arr_2
del arr_3

print(gc.collect())
gc.enable()






print('Собрано до создания графа:', gc.collect())

#практическая задача
dict_1 = {}
dict_2 = {}
dict_3 = {}
dict_4 = {}

dict_1['key'] = [dict_2]
dict_2['key'] = [dict_3]
dict_3['key'] = [dict_1]


print(dict_1['key'][0] is dict_2)
print(dict_2['key'][0] is dict_3)
print(dict_3['key'][0] is dict_1)

del dict_1
del dict_2
del dict_3

print('Собрано после удаления графа:',gc.collect())

print('Независимый узел:', dict_4)