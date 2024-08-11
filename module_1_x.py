grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_s = sorted(list(students))
grades_a = []
for stud in grades:
    avg = sum(stud) / len(stud)
    grades_a.append(avg)
dict_j = dict(zip(students_s, grades_a))
print(dict_j)
