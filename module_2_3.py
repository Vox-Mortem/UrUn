my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
lst_index = 0
while lst_index < len(my_list):
    if my_list[lst_index] < 0:
        break
    if my_list[lst_index] > 0:
        print(my_list[lst_index])
        lst_index += 1
    else:
        lst_index += 1
