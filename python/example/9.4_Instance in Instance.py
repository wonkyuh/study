## 객체 속의 객체
# 클래스를 본따 만든 객체 하나하나를 인스턴스라고 한다.
# 즉 인스턴스가 객체다.

class Fridge:
    def __init__(self):
        self.isOpened = False
        self.foods =[]
        
    def open(self):
        self.isOpened = True
        print('냉장고 문을 열었어요.')
        
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print('냉장고 속에 음식이 들어갔네...')
        else:
            print('냉장고 문이 닫혀있어서 못넣겠어요...')
    def close(self):
        self.isOpened = False
        print('냉장고 문을 닫았어요...')
        
class Food:
    pass

# 현재 냉장고 객체 안에 foods라는 리스트를 갖고 있고,
# 아래 결과 apple과 orange의 인스턴스. 즉, 객체가

f = Fridge()
apple = Food()
orange = Food()
f.open()
f.put(apple)
f.put(apple)
f.close()
print(f.foods)

f.__init__() # 초기화


