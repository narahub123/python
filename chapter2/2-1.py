
a = 123
print(type(a)) # int

b=1.2
print(type(b)) # float

c = 4.25E10
print(type(c)) # float

#8진수 
d = 0o10
print(type(d)) #int
print(d) #8

#16진수
e = 0x8ff
print(e) #2303

# 사칙 연산
a = 3
b = 4
print(a + b) #7
print(a * b) #12
print (a / b) #0.75
print (a ** b) # 81
print (a // b) #0 몫
print (a % b) #3 나머지

# 문제 
# 14를 3으로 나누었을 때 몫과 나머지
# 몫 
print("몫", 14 // 3)
# 나머지 
print("나머지", 14 % 3)