a = [1, 2, 3]

# b= a
# a[1] = 4

# print(a) # [1, 4, 3]
# print(b) # [1, 4, 3]

# 슬라이싱
# b = a[:]

# a[1] = 4

# print(a) # [1, 4, 3]
# print(b) # [1, 2, 3]

# copy

a = [1, 2, 3]
b = a.copy()

a[1] = 4

print(a) # [1, 4, 3]
print(b) # [1, 2, 3]

(a, b) = ('python', 'life')

print(a) # python
print(b) # life

a =  b = 'python'

print(a) # python
print(b) # python

a = 3
b = 5
a, b = b, a

print(a) # 5
print(b) # 3