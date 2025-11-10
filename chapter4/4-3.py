# 파일 쓰고 읽고 수정하기 

# 파일 생성하기 
# f = open("새파일.text", 'w')

# f.close()

# 파일 객체 = open("파일_이름", "파일_열기_모드")

# 파일 생성하기 파일 결로 지정하기 
# f = open("doit/새파일.txt", 'w')

# f.close()

# f = open('doit/새파일.txt', 'w', encoding='utf-8')

# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" %i
#     f.write(data)
# f.close()

## 파일을 읽는 여러가지 방법 
# # 한 줄 읽기
# f = open('doit/새파일.txt', 'r', encoding='utf-8')

# line = f.readline()

# print(line) # 1번째 줄입니다.

# f.close()

# 여러 줄 읽기
# f = open('doit/새파일.txt', 'r', encoding='utf-8')

# while True: 

#     line = f.readline()

#     if not line:
#         break

#     print(line) 

# f.close()

# 1번째 줄입니다.

# 2번째 줄입니다.

# 3번째 줄입니다.

# 4번째 줄입니다.

# 5번째 줄입니다.

# 6번째 줄입니다.

# 7번째 줄입니다.

# 8번째 줄입니다.

# 9번째 줄입니다.

# 10번째 줄입니다.

# 여러 줄 읽기
# f = open('doit/새파일.txt', 'r', encoding='utf-8')

# lines = f.readlines()

# for line in lines:
#     line = line
#     print(line)

# f.close()

# read
# f = open('doit/새파일.txt', 'r', encoding='utf-8')

# data = f.read()

# print(data)

# f.close()

# 1번째 줄입니다.
# 2번째 줄입니다.
# 3번째 줄입니다.
# 4번째 줄입니다.
# 5번째 줄입니다.
# 6번째 줄입니다.
# 7번째 줄입니다.
# 8번째 줄입니다.
# 9번째 줄입니다.
# 10번째 줄입니다.

# 파일 객체를 for문과 함께 사용하기 

# f = open('doit/새파일.txt', 'r', encoding='utf-8')

# for line in f: 
#     print(line)

# f.close()

# # 1번째 줄입니다.

# # 2번째 줄입니다.

# # 3번째 줄입니다.

# # 4번째 줄입니다.

# # 5번째 줄입니다.

# # 6번째 줄입니다.

# # 7번째 줄입니다.

# # 8번째 줄입니다.

# # 9번째 줄입니다.

# # 10번째 줄입니다.

# f = open('doit/새파일.txt', 'a', encoding='utf-8')

# for i in range(11, 20):
#     data= "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# with open('doit/새파일.txt', 'a', encoding='utf-8') as f:
#     f.write("Life is too short, you need python")

