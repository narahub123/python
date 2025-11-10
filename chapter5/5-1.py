# result = 0

# def add(num):
#     global result
#     result += num
#     return result

# print(add(3)) # 3

# print(add(4)) # 7


# # 계산기 더하기 
# result1 = 0
# result2 = 0

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2


# print(add1(3)) # 3
# print(add1(4)) # 7
# print(add2(7)) # 7
# print(add2(4)) # 11

# 클래스 만들기 
class Cookie:
    pass

# 객체 (instance)
초코쿠키 = Cookie()
아몬드쿠키 = Cookie()

# 계산기 만들기 
# class FourCal:
#     # 함수
#     def setData(self, first, second):
#         self.first= first # 객체 변수, 속성
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result
    
#     def sub(self):
#         result = self.first - self.second
#         return result
    
#     def mul(self):
#         result = self.first * self.second
#         return result
    
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# b = FourCal()

# print(type(a)) # <class '__main__.FourCal'>

# a.setData(4, 2)
# b.setData(6, 5)

# print(a.first) # 4
# print(a.second) # 2

# print(a.add()) # 6
# print(a.sub()) # 2.0
# print(a.mul()) # 8
# print(a.div()) # 2.0

# print(b.add()) # 11
# print(b.sub()) # 1
# print(b.mul()) # 30
# print(b.div()) # 1.2


class FourCal:
    # 생성자
    def __init__(self, first, second):
        self.first= first # 객체 변수, 속성
        self.second = second
    # 함수
    def setData(self, first, second):
        self.first= first # 객체 변수, 속성
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal(4, 2)

# 상속 
class MOreFourCal(FourCal):
    pass
a = MOreFourCal(4, 2)
print(a.sub()) # 2

# 자기 자신의 함수 추가 
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
a = MoreFourCal(4, 2) 

print(a.pow()) # 16

# 오버라이딩 
# a = MoreFourCal(4, 0)
a.div()

class SaveFourCal(FourCal):
    def div (self):
        if(self.second == 0):
            return 0
        else :
            return self.first / self.second
a = SaveFourCal(4, 0)
print(a.div()) # 0

# 클래스 변수 
# 공통적으로 가지고 있는 값 
class Family:
    lastname = "김"

a = Family()
b = Family()

a.lastname = "박"

print(a.lastname) # 박
print(b.lastname) # 김 