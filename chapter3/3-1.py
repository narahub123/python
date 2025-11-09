money = True

if money:
    print('택시를 타고 가라')
else:
    print('걸어 가라')

# 택시를 타고 가라

money = False

if money:
    print('택시를 타고 가라')
else:
    print('걸어 가라')

# 걸어 가라

# 비교 연산자
x=3
y=2
print(x < y)
print(x != y)

money = 2000
if money > 3000:
    print('택시를 타고 가라')
else:
    print('걸어 가라')

# or
money = 2000
card = True

if money > 3000 or card:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
# 택시를 타고 가라

# or
money = 2000
card = True

if money > 3000 and card:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
# 걸어 가라

# not 
money = 2000
card = True

if not money:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
# 걸어 가라

print (1 in [1, 2, 3]) # True
print(1 not in [1, 2, 3]) # False

# elif
pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket:
    print("택시를 타고 가라")
elif 'card':
    print("택시를 타고 가라")
else:
    print('걸어가라')

    pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket: pass
else: print('걸어가라') 
# 걸어가라

score = 100

if score >= 60:
    message = 'success'
else : 
    message = "failure"

print(message)

# 한 줄로 

message = 'success' if score >= 60 else "failure"

print(message)

    