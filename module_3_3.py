# 1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(8)
print_params(9, 5)
print_params('plk', True, 13)
print_params(b=25)
print_params(c=[1, 2, 3])
print('--------------------------------------------------------------------------')

# 2
values_list = [False, 33, 'navy']
values_dict = {'a': 11, 'b': True, 'c': 'seal'}
print_params(*values_list)
print_params(**values_dict)
print_params(c=[1, 2, 3])
print('--------------------------------------------------------------------------')

# 3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
