def add(a, b): # 매개 변수(parameter)
    result = a + b
    return result

print(add(1, 2)) # 3 # 인수(argument)

# 입력 값이 없는 함수 
def say():
    return 'Hi'

print(say()) # Hi

# 리턴 값이 없는 함수 
def add(a, b):
    print('%d, %d의 합은 %d입니다.' % (a, b, a+b))

a = add(1,2) # 1, 2의 합은 3입니다.

print(a) # None

# 매개변수를 지정해서 호출 
def sub(a, b):
    return a - b

a = sub(a=7, b=3)
a = sub(b=3, a=7)

print(a) # 4

def add_many(*args):
    result = 0

    for i in args:
        result += i
    
    return result

print(add_many(1, 2, 3)) # 6


def add_mul (choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul('add', 1, 2, 3, 4)

print(result) # 10

# 키워드 매개변수 , kwargs
def print_kwargs(**kwards):
    print(kwards)

print_kwargs(a=1, b=2) # {'a': 1, 'b': 2}

# 초기값 설정하기 
def say_myself(name, old, man = True):
    print('나의 이름은 %s 입니다.' % name)
    print('나이는 %d 입니다.' % old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself("조코딩", 20, False)

# 나의 이름은 조코딩 입니다.
# 나이는 20 입니다.
# 여자입니다.

a = 1
def vartest(a):
    a += 1

vartest(a)
print(a) # 1

a = 1
def vartest(a):
    a += 1
    return a

a = vartest(a)
print(a) # 2

a = 1
def vartest():
    global a 
    a += 1

vartest()
print(a) # 2

b = [1, 2, 3]

def vartest2(b):
    b = b.append(4)

vartest2(b)

print(b) # [1, 2, 3, 4]

add = lambda a, b: a+b

result = add(3, 4)

print(result) # 7