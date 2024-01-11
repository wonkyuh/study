## 상속

class Person:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    
    def eat(self):
        print('냠냠')
    def sleep(self):
        print('쿨쿨')
    def talk(self):
        print('주절주절')
    
# 파이썬 상속은 단순히 괄호 안에 클래스를 담기만 하면 되네?
class Student(Person):
    def study(self):
        print('공부')

hong = Person()
kim = Student()
hong.eat()
# hong.study()
kim.eat()
kim.study()

# 상속은 Student *is a* Person 이렇게 표현된다.
# [하위 클래스] is a [상위 클래스]





    