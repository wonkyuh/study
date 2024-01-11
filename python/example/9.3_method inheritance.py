## 메서드 상속과 재정의
# 재정의 = override (오버라이드)
# 상위 클래스에 있는 메서드를 재정의하는 것을 말한다.
class 동물:
    def 울어(self):
        print('...')

class 고양잇과(동물):
    pass

class 호랑이(고양잇과):
    def 울어(self):
        print('어흥')
        
class 고양이(고양잇과):
    def 울어(self):
        print('야옹')
        
포돌이 = 호랑이()
포돌이.울어()

은콩이 = 고양이()
은콩이.울어()

# isistance
# 특정 클래스의 인스턴스인지 판별해주는 함수 (True or False)

print(isinstance(은콩이, 고양이))
print(isinstance(은콩이, 호랑이))

