immutable_var = 1, 2, 'Word', True
print(immutable_var)
print(type(immutable_var))
#immutable_var[0] = 3         оставлю комментарием, иначе программа дальше не выполняет код.
#print(immutable_var)
#Кортеж относится к неизменяемым объектам и не поддерживает обращение по элементам,
#а служит больше для хранения информации, которую мы не хотим менять. Можно изменять изменяемые объекты внутри кортежа.
mutable_list = [1, 2, 'Word', True]
print(mutable_list)
print(type(mutable_list))
mutable_list[2] = 2
print(mutable_list)