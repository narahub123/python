# 문자열 
a = 'Life is too short, You need Python'
b = "a \""
c = '123'

print(type(a)) #str
print(type(b)) #str
print(type(c)) #str

# 여러 줄인 문자열을 변수에 대입하고 싶을 때 
# 줄바꿈 
a = 'Life is too short, \n You need Python'
a = '''Life is too short, 
You need Python'''

print(a)

# 문자열 연산 

# 문자열 연산하기 
head = "Python"
tail = " is fun!"
print(head + tail)

# 문자열 반복 
print(head * 3)

# 응용
print('='* 50)
print('My program')

# 길이 구하기 
print(len(a)) #35

# 문자열과 인덱스
print(a[3])

# 문자열 슬라이싱 : js의 slice와 비슷 간격 개념만 추가로 이해하면 됨
print(a[0:4])
print(a[0:4:2]) # 이상:미만:간격
print(a[::2])
print(a[::-1])
print(a[9:-7])

# 문자열 포매팅 

a = 'I eat %d apples' % 5
print(a)
number = 3
day = 'five'

b = "I ate %d apples. so I was sick for %s days" % (number, day)

print(b)

# 문자열 포맷 코드 
# %s 
# %d
# %c
# %%

# 포맷 코드와 숫자 함께 사용하기 
a = '%10s' % 'hi'
b = '%-10s' % 'hi'

print(a)
print(b)

# 소수점 표시 
a = "%0.4f" % 3.42134234
print(a)

# .format

a = "I eat {0} apples" .format(5)

number = 10
day = 'three'
a = "I eat {0} apples. I'm sick for {1} days" .format(number, day)

print(a)

# 왼쪽 정렬 

# 오른족 정렬

a = '{0:<10}' .format('hi')
print(a)
a = '{0:>10}' .format('hi')
print(a)
a = '{0:^10}' .format('hi')
print(a)
# 공백 채우기
a = '{0:$^10}' .format('hi')
print(a)

# f 문자열 포맷팅 
name = "홍길동"
age = 30

a = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(a)

a = f'{"hi":_^10}'
print(a)

# 문자열 관련 함수들 

#문자열 개수 세기 (count)
a = 'hobby'
print(a.count('b'))

# 위치 알려주기
print(a.find('b')) # 없는 문자를 삽입하면 -1

print(a.index('b')) # 없는 문자를 삽입하면 오류

a=', '.join('abcd') # a, b, c, d
print(a)

a = ", ".join(['a', 'b', 'c', 'd']) # a, b, c, d
print(a)

# 소문자 대문자 바꾸기: upper, lower
a = 'hi'
print(a.upper())

# 공백 지우기 
a = " hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# 문자열 바꾸기
a = 'Life is to short'

print(a.replace('Life', 'Your leg'))

# 문자열 나누기 
print(a.split())
a = 'a:b:c:d'
print(a.split()) # ['a:b:c:d']
print(a.split(":")) # ['a', 'b', 'c', 'd']
