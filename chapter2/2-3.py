# 리스트 
odd = [1, 3, 5, 7, 9]
print(type(odd))

e = [1, 2, ["Life", "is"]]
print(e)

# 인덱스
a = [1, 2,3]

print(a[1])
print(a[1] + a[2])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3]) # ['a', 'b', 'c']
print(a[3][1]) # b

# 슬라이싱 
a = [1, 2, 3, 4, 5]
print(a[0:2]) # [1, 2]
print(a[0:2:2]) # [1]
print(a[::2]) # [1, 3, 5]

# 연산하기 
# 리스트 더하기 
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # [1, 2, 3, 4, 5, 6]
# 리스트 곱하기 
a = [1, 2, 3]
b = 3
print(a * b) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 길이 구하기 
a = [1, 2, 3]
print(len(a)) #3

# 서로 다른 자료형의 연산 안됨 

# 리스트의 수정 
a = [1, 2, 3]
a[2] = 4
print(a) # [1, 2, 4]

# 리스트의 삭제 (del)
del a[1]

print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a) # [1, 2]

# 메서드 
# 리스트에 요소 추가하기 (append)
a = [1, 2, 3]
a.append(4) # [1, 2, 3, 4]
a.append([2, 3]) # [1, 2, 3, 4, [2, 3]]
print(a)

# 정렬 (sort)
a= [1, 4, 3, 2]
a.sort()

print(a) # [1, 2, 3, 4]
a = ['a', 'c', 'b']

a.sort()
print(a) # ['a', 'b', 'c'] 

# 뒤집깁
a = ['a', "c", 'b']
a.reverse() # ['b', 'c', 'a']

a.sort() # ['a', 'b', 'c']
a.reverse() # ['c', 'b', 'a']
print(a) 

# 인덱스 반환 index 
a = [1, 2, 3]
print(a.index(3)) # 2

# 요소 삽입 insert 
a = [1, 2, 3]
a.insert(0, 4)

print(a) # [4, 1, 2, 3]

# 요소 제거 remove : 리스트에서 첫 번째 요소를 삭제

a = [1, 2, 3, 4, 5, 6]
a.remove(3)

print(a) # [1, 2, 4, 5, 6]

# 리스트 요소 끄집어 내기 pop
a = [1, 2, 3]
print(a.pop()) # 3
print(a) # [1, 2]

print(a.pop(1)) # 2
print(a) # [1]

# 세기 
a = [1, 2, 3, 1]
print(a.count(1)) # 2

# extend 
a = [1, 2, 3]
a.extend([4, 5])
print(a) # [1, 2, 3, 4, 5]
