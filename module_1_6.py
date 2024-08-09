# словарь
my_dict = {'beer': 250, 'pork': 400, 'chips': 140}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('beer'))
print('Not existing value:', my_dict.get('cherry', 'ключ не найден'))
my_dict.update({'cheese': 685, 'peanut': 358})
x = my_dict.pop('pork')
print('Deleted value:', x)
print('Modified Dict:', my_dict, '\n')
# множество
my_set = {1, 2, 3, 2, 2.5, 'sad', (4, 5, 5), 'happy', (4, 5, 5), 'sad', True}
print('Set:', my_set)  # bool не выводит даже в уроке
my_set.update([13, 'by'])
my_set.remove('sad')
print('Modified Set:', my_set)
