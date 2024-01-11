## __init__ 메서드 (초기화)

# --------------------------------------------
# 최종결론
# 초기화 어렵게 생각할 필요 없이
# 처음에 인자를 받아 변수를 결정(정의?)하며
# 인스턴스를 시작하게 해주는 메서드이다.
# --------------------------------------------

# 메서드 초기화라는 말이 낯설게 느껴졌지만
# 초기화는 0의 상태로 만드는 것이 아닌
# 최초 변수를 정의하는 것이라고 볼 수 있다.

# 다른 언어에서 이 초기화를 "생성자"라고 말한다.
# 생성자는 객체 지향 프로그래밍에서 객체의 초기 상태를
# 설정하고 필요한 초기화 작업을 수행하는데 사용되며, 
# 코드의 가독성과 유지보수성을 향상시킵니다.

class Book:
    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
        
    def printData(self):
        print('제목 :',self.title)
        print('가격 :',self.price)
        print('저자 :',self.author)
        
    def __init__(self, title, price, author):
        self.setData(title, price, author)
        self.printData()
        print('책 객체를 새로 만들었습니다.')
            
    # def __init__(self):
    #     print('책 객체를 초기화합니다.')     
         

        
# 초기화 사용 전에는
# 인스턴스를 정의하고 데이터를 입력하는 메서드를 진행하고
# 출력하는 메서드까지 써야했다면
# HongLibrary = Book()
# HongLibrary.setData('Lord Of The Rings','38900','Tolkien')
# HongLibrary.printData()


# 인스턴스를 정의함과 동시에 변수를 정의할 수 있다.
HongLibrary = Book('Harry Porter','22000','Rowling')

KimLibrary = Book('Lord Of The Rings','38900','Tolkien')

## __del__ 메서드 (소멸자)

class delBook(Book):
    def __del__(self):
        print('객체가 소멸되었습니다.')

LeeLibrary = delBook('X-man','54000','Marvel')
# 인스턴스(객체)를 더 이상 참조하지 않을 때
# __del__ 메서드가 자동으로 실행된다.

## __repr__ 메서드 (프린팅)
class reprBook(Book):
    def __repr__(self):
        return self.title
    
ParkLibrary = ('Lost','43200','Lora')
print(ParkLibrary)

## __add__ 메서드 (덧셈)
# 단순하게 숫자가 연산되는 것처럼 보일 수 있지만
# 클래스를 통해 만든 객체에 대해서도
# 연산자를 쓸 수 있게 된 예제이다.

class Shape:
    area = 0
    
    def __add__(self,other):
        return self.area + other.area
    
    def __sub__(self,other):
        return self.area - other.area

a = Shape()
a.area = 20
b = Shape()
b.area = 10

print(a+b)
print(a-b)

## __lt__ 메서드 (비교)
# 객체를 서로 비교할 수 있는 메서드
class shape:
    area=0
    def __lt__(self,other):
        return self.area < other.area
    
c = shape()
c.area = 30
d = shape()
d.area = 20
print(c>d)
if c > d : print('c가 더 넓어요')

