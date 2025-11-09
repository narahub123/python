treeHit = 0

while treeHit < 10:
    treeHit += 1
    print('나무를 %d번 찍었습니다.' % treeHit)
    if treeHit == 10:
        print('나무 넘어갑니다.')

prompt = '''
1. Add
2. Del
3. List
4. Quit
Enter number: 
'''

number = 0
while number !=4:
    print(prompt)
    number = int(input())

# 강제로 빠져 나가기
coffee = 10
money = 300

while money:
    print('돈을 받았이니 커피를 줍니다.')
    coffee -= 1
    print('남은 커피의 양은 %d개입니다.' % coffee)
    if coffee == 0:
        print('커피가 떨어졌습니다. 판매를 중지힙니다.')
        break

a = 0
while a < 10:
    a += 1
    if a % 2 == 0: 
        continue
    print(a)
# 1
# 3
# 5
# 7
# 9