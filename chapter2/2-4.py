# 변경, 삭제 불가 
# 만드는 방법
t1 = ()
print("t1의 타입", type(t1))
t2 = (1,)
print("t2의 타입", type(t2))
print("인덱싱", t2[0])
t3 = (1, 2, 3)
t4 = 1, 2 ,3
print("t4의 타입", type(t4))
t5 = ('a', 'b', ('ab', 'cd'))

# 삭제 
t1 = (1, 2, 'a', 'b')
# del t1[0]
# Traceback (most recent call last):
#   File "d:\projects\python\chapter2\2-4.py", line 7, in <module>
#     print("인덱싱", t1[0])
#                  ~~^^^
# IndexError: tuple index out of range

#인덱싱 
print(t1[2]) # a

# 슬라이싱  
print(t1[1:]) # (2, 'a', 'b')
print(t1) # (1, 2, 'a', 'b') 

# 더하기 
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2

print("t1", t1) # t1 (1, 2, 'a', 'b')
print("t2", t2) # t2 (3, 4)
print("t3", t3) # t3 (1, 2, 'a', 'b', 3, 4)

# 곱하기 

t3 = t2 * 3

print(t3) # (3, 4, 3, 4, 3, 4)

# 길이
print(len(t3)) # 6
