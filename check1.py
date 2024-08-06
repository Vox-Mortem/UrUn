# 1
example = 'Cemetery'
# 2
print(example[0])
# 3
print(example[-1])
# 4
x = len(example[(len(example)+1)//2-1:])
if x % 2 == 0:
    print(example[(len(example)+1)//2:])
else:
    print(example[(len(example)+1)//2-1:])
# 5
print(example[::-1])
# 6
print(example[1::2])
