## 객체 : 자신 고유의 속성을 갖는 물리적, 추상적인 모든 대상
## 클래스 : 객체들을 SW 내에 구현하기 위해 만든 설계도
## 메서드 : 클래스 안에 정의하는 함수
## 인스턴스 : 클래스를 통해 생성한 객체

## 클래스

class Singer:               # 클래스 정의
    def sing(self):         # 메서드 정의
        return "LaLaLa"

taeji = Singer()            # 객체(인스턴스) 정의
# print(taeji.sing())         # 클래스의 메서드 사용

ricky = Singer()
# print(ricky.sing())

## 변수와 메서드
class Amazon:
    strength = 20
    dexterity = 25
    vitality = 20
    energy = 15
    
# 메서드를 만들 떄 첫 번째 매개변수를 self로 한다.    
    def attack(self): 
        print('Jab!') 
        
# if, 매개 변수를 두 개 가져가야 할 경우
    def attack(self, damage):
        total_damage = damage + self.strength
        return f'Jab for {total_damage} damage!!!'

                
    def exercise(self):
        self.strength +=2
        self.dexterity +=3
        self.vitality +=1

jane = Amazon()
mary = Amazon()
print(jane.attack(10))
jane.exercise()
print(jane.strength)