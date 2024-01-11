## tuple

# 두 변수를 서로 바꾸기
c, d = 10, 20
c, d = d, c
print(c,d)

# 마구 찍어 함수
def magu_print(x,y, *rest):
    print(x,y,rest)
    
magu_print(1,2,3,4,5,6,7,8,9,10)

# 튜플 문법
t = ('a','b','c')
print(t)
empty=()
print(empty)
one = 5, 
print(one)

# 튜플은 원소 값을 직접 바꿀 수 없기 때문에, 오려 붙이는 방법을 써야함.
p=(1,2,3)
q=p[:1]+(5,)+p[2:]
print(p)
print(q)

# 튜플을 리스트로, 리스트를 튜플로 쉽게 바꿀 수 있다.
p=list(p)
print(p)
p=tuple(p)
print(p)

##############################################################

## 연습문제
# 1. 날짜를 나타내는 세 개의 숫자를 입력 받는다.
# 2. 입력 받은 날짜를 mm/dd/yyyy 형식으로 출력한다.
# 3. 내일 날짜까지 출력한다. (각 ㅇ)

# def read_date():
#     year, month, day = tuple(map(int, input().split()))
#     return year, month, day

# def print_date(date):
#     year, month, day = date
#     print("%02d/%02d/%04d" % (month, day, year))

# def advence_day(date):
#     year, month, day = date
#     endofmonth=(month,day) in [(1,31), (2,28), (3,31),(4,30),(5,31),(6,30),(7,31),
#                                (8,31),(9,30),(10,31),(11,30),(12,31)]
#     endofyear= month==12 and day==31
    
#     if endofmonth:
#         if endofyear:
#             year+=1
#             month=1
#             day=1
#         else:
#             month+=1
#             day=1
#     else:
#         day+=1
#     return year,month,day
# today=read_date()
# print_date(today)
# tomorrow = advence_day(today)
# print_date(tomorrow)