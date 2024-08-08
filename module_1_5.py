immutable_var = 32, 'Deliverance', True
print(immutable_var)
# tuple[0] = 11
# print(immutable_var) #TypeError: 'tuple' object does not support item assignment
mutable_list =([44, 'Corrupt', False, ], 322)
print(mutable_list)
mutable_list[0][1] = 'Curse'
print(mutable_list)
