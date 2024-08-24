data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

s_sum = 0


def calculate_structure_sum(source):
    global s_sum
    if isinstance(source, dict):
        for value in source.values():
            calculate_structure_sum(value)
        for key in source.keys():
            calculate_structure_sum(key)
    elif isinstance(source, list) or isinstance(source, tuple) or isinstance(source, set):
        for item in source:
            calculate_structure_sum(item)
    elif isinstance(source, int) or isinstance(source, str):
        if isinstance(source, int):
            s_sum += source
        elif isinstance(source, str):
            s_sum += len(source)

    return s_sum


result = calculate_structure_sum(data_structure)
print(result)
