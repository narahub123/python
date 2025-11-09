dic =  {'name': "pey", 'phone': "000-0000-0000", 'birth': "1111"}

print(type(dic)) # <class 'dict'>

# 추가
a = {1 : 'a'}

a[2] = 'b'

print(a) # {1: 'a', 2: 'b'}

# 삭제 
a = {1 : 'a', 2: 'b', 'name': "pey", 3: [1,2,3]}

# del a['name'], a[2]

print(a) # {1: 'a', 3: [1, 2, 3]}

grade = {'pey': 10, 'julliet': 99}

print(grade['pey']) # 10

# 함수 
print(a.keys()) # dict_keys([1, 2, 'name', 3])

print(a.values()) # dict_values(['a', 'b', 'pey', [1, 2, 3]])

print(a.items()) # dict_items([(1, 'a'), (2, 'b'), ('name', 'pey'), (3, [1, 2, 3])])

# print(a.clear()) # None 

print(a.get('name')) # pey
print(a.get('nam', '값이 없습니다.')) # 값이 없습니다.
# 없는 키를 넣은 경우 None

print('name' in a) # True