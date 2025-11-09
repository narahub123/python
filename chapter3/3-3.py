test_list = ['one', 'two', 'three']

for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]

for(first, last) in a:
    print(first, last)
# 1 2
# 3 4
# 5 6

marks = [90, 25, 57, 45, 80]

number = 0

for mark in marks:
    number += 1
    if mark < 60:
        continue
    print('%d번 학생 축하합니다. 합격입니다.' % number)

# 1번 학생 축하합니다. 합격입니다.
# 5번 학생 축하합니다. 합격입니다.

# range
add = 0
for i in range(1, 11):
    add += i

print(add) # 55

# 구구단 
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')
# 2 4 6 8 10 12 14 16 18
# 3 6 9 12 15 18 21 24 27
# 4 8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54
# 7 14 21 28 35 42 49 56 63
# 8 16 24 32 40 48 56 64 72
# 9 18 27 36 45 54 63 72 81

a = [1, 2, 3, 4]

result = []

for num in a:
    result.append(num * 3)

print(result) # [3, 6, 9, 12]

a = [1, 2, 3, 4]
result = [num * 3 for num in a]

print(result) # [3, 6, 9, 12]