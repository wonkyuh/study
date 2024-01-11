# a_list=[1,3,5,7,2,8,4,5,6,7,9,7,6,1]
# # print(len(a_list))

# def print_list(a):
#     for i in a:
#         print(i)

# print_list(a_list)

# def test(x,y):
#     if x>y:
#         print(f'{x}가 {y}보다 큽니다.')
#     elif x<y:
#         print(f'{x}가 {y}보다 작습니다.')
#     elif x==y:
#         print(f'{x}와 {y}는 같습니다.')
# test(10,10)
# num=str(256**4)
# print(len(num))

# num2=str(2**128)
# print(len(num2))

# def numOfDigits(x):
#     print(len(x))

# numOfDigits(str(input()))

# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i} * {j} = {i*j}')
        
## 한단을 계산하는 함수
# def multi(m):
#     for i in range(1,10):
#         print(f'{m}*{i}={m*i:2}')
        
# multi(2)

# def f1(x):
#     a=3
#     b=5
#     y=a*x+b
#     return y

# print(f1(10))

# def triangle(x,y):
#     A=x*y/2
#     return A


# def korean_number(i):
#     i_list=['일','이','삼','사','오','육','칠','팔','구','십']
#     print(i_list[i-1])

# korean_number(int(input()))

# def triple(x):
#     print(x+x+x)
    
# triple(2)

# def simple_interest(x,y,z):
#     return (x+(x*y))*z

# print(simple_interest(10000,0.5,3))

# a1='wonkyo'
# a1='hong'
# print(a1)

## 전역변수
# jjang='pig dad'
# def ban():
#     print('jjang = ',jjang)
    
# ban()

## 지역변수
# def ban():
#     jjang='07'
#     print('jjang = ',jjang)
    
# ban()

## 전역변수로 선언하기 (global)
# def e_is_10():
#     global e
#     e = 10
#     print('e값은 ', e, '입니다')
    
# e_is_10()
# print(e)

## Lambda

# def hap(x,y):
#     return x+y

# print(hap(10,20))

# lambda x,y: x+y)(10,20)
# print((lambda x,y: x+y)(10,20))

## map(함수,리스트)
# 리스트에서 하나씩 꺼내 함수를 돌리고 다시 넣음
# list(map(lambda x:x ** 2 ,range(5)))

## reduce(함수, 시퀀시)
# 리스트,튜플 문자열 등 누적 연산
# from functools import reduce
# print(reduce(lambda x,y:x+y,[0,1,2,3,4]))

# print(reduce(lambda x,y:y+x,'abcde'))

## filter(함수,리스트)
# 함수 결과 시 참인 값들로 리스트 재구성

# list(filter(lambda x:x<5, range(10)))
# print(list(filter(lambda x:x<5, range(10))))
# print(list(filter(lambda x:x%2==0,range(10))))

## 함수 예제
# def read(x):
#     y=x.replace('~',':')
#     a=y.replace('cm','')
#     b=a.replace(' ','')
#     # 앞뒤 공백을 제거하고 싶으면 str.strip(" I am a boy. ")
#     i=b.split(':')
#     ridename=i[0]
#     cmmin=i[1]
#     cmmax=i[2]
#     return ridename, cmmin, cmmax

# if __name__=="__main__":
#     ridename, cmmin, cmmax = read(str(input('놀이 기구 이름과 제한 키 정보를 입력하시오. ')))
#     print("이름 : ",ridename)
#     print("최소 : ", cmmin)
#     print("최대 : ", cmmax)

def rideread(text):
    ridename, limit = map(str.strip, text.split(':')) 
    # 입력 받은 text를 : 기준으로 나누어 리스트에 담기 전에d
    # str.strip을 통해 앞뒤 공백을 제거하고 담는다.
    
    cmmin=cmmax=None # 변수를 정의하고
    if '~' in limit: # 만약 ~가 limit 값에 포함되어 있다면
        templist=[]
        for x in limit.split('~'): # ~ 기준으로 나뉜 리스트를 for반복하여
            templist.append(x.replace('cm','')) # cm를 제거한 값을 templist에 추가한다.
        cmmin, cmmax = templist[0], templist[1] # 그래서 templist의 [0], [1]을 각각 변수로 정의한다.
    elif '이상' in limit: # 만약 이상이 limit 값에 포함되어 있다면 
        cmmin = int(limit.split("cm")[0]) # cm

    return ridename, cmmin, cmmax

# if __name__=="__main__":
ridename, cmmin, cmmax = rideread(str(input('놀이 기구 이름과 제한 키 정보를 입력하시오. ')))
print("이름 : ",ridename)
print("최소 : ", cmmin)
print("최대 : ", cmmax)