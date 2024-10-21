my_dict = {'Alex' : 1997, 'Minerva': 1990, 'Lena': 1996}
print('Словарь:', my_dict)
print('Существующий ключ:', my_dict.get('Alex'))
print('Несуществующий ключ:', my_dict.get('Diana'))
my_dict.update({'Reinold': 1994,
                'Roman': 2000})
deleted_value = my_dict.pop('Alex')
print('Удалённый ключ:', deleted_value)
print('Новый словарь:', my_dict)

my_set={1,2,4, 'apple', 'peach',2, 'peach', 4, 'apple'}
print('Множество:', my_set)
my_set.add(5)
my_set.add('orange')
my_set.discard('apple')
print('Новое множество:', my_set)