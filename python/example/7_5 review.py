
## 5 ~ 6 리뷰 시간

a_list=[1,3,5,7,9,]
print(len(a_list))

def printlist(a):
    for i in a:
        print(i)

printlist(a_list)        

def test(x,y):
    if x>y:
        print(f'{x}는 {y}보다 크다.')
    elif x<y:
        print(f'{x}는 {y}보다 작다.')
    elif x==y:
        print(f'{x}는 {y}와 같다.')

test(9,10)

num=str(256**4)
print(len(num))

def numofDigit(a):
    print(len(a))
    
numofDigit(num)

# 구구단
# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i}*{j}={i*j}')
        
# 한 단을 계산하는 함수
def multi(a):
    for i in range(1,10):
        print(f'{a}*{i}={a*i}')

multi(2)

def koreanNum(a):
    k_list=['일','이','삼','사','오']
    print(k_list[a-1])
koreanNum(2)

def triple(x):
    print(x*3)

triple(2)

# 전역변수
jjang='pig dad'
def ban():
    print('jjang = ',jjang)
    
ban()

# 지역변수
def ban():
    jjang='07'
    print('jjang = ',jjang)
    
ban()

def e_is_10():
    global e
    e=10
    print('e값은 ',e,' 입니다.')
e_is_10()
print(e)

## Lambda

def hap(x,y):
    return x+y
print(hap(3,2))

((lambda x,y:print(x+y))(10,20))

## map
# 리스트에서 하나씩 거내 함수를 돌리고 다시 넣음
A=list(map(lambda x:x*3,range(1,10)))
print(A)
# map 함수는 Lambda 함수와 연동해서 잘 쓰인다.

## reduce(함수,시퀀스)
# 누적 연산 함수!! 시퀀스 모든걸 합친다
from functools import reduce
print(reduce(lambda x,y:y+x,[0,1,2,3,4,5]))
# 여기서 시퀀스란 list, tuple, 문자열

# reduce 문자열 합쳐보기
print(reduce(lambda x,y:x+y,['I',' ','L','O','V','E',' ','U']))
print(reduce(lambda x,y:x+y,{'I',' ','L','O','V','E',' ','U'}))
# set는 Unordered한 성질을 갖는다. 즉, 순서가 없다.

## filter(함수,리스트)
# 함수 결과 시 참인 값들로 리스트 재구성
print(list(filter((lambda x:x<5),[3,4,5,6])))

## 다시 정리 #########################

## map 함수 
# 함수 연산 후 다시 리스트 담기

## reduce 함수
# 시퀀스 누적 함수 연산

## filter 함수
# 함수 결과 참인 값들만 리스트 담기

######################################

# def read(x):
#     # split 함수를 이용한 리스트 만들기
#     # "놀이기구이름: 최소 키 ~ 최대 키"를 입력 받았을 때
#     # "놀이기구이름:최소 키:최대 키"로 변환해주고
#     # ':' 기준으로 쪼개 리스트에 담는다.
#     y=x.replace('~',':')
#     a=y.replace('cm','')
#     b=a.replace(' ','')
#     i=b.split(':')
#     ridename=i[0]
#     cmmin=i[1]
#     cmmax=i[2]
    
#     return ridename, cmmin, cmmax

# ridename, cmmin, cmmax =read(input())
# print(f'놀이기구 이름 : {ridename}')
# print(f'최소 키 : {cmmin}cm')
# print(f'최대 키 : {cmmax}cm')

def rideread(text):
    # 두 가지 변수를 받는데
    # 입력된 text를 ':' 기준으로 쪼개어 리스트에 담고
    # 문자열로 리스트를 변환하는 함수를 연산하여 다시 리스트
    ridename, limit = map(str.strip, text.split(':'))
    
    cmmin=cmmax=None
    if '~' in limit: # limit(즉, 키 제한 부분)에 '~'가 포함되어 있다면
        templist=[]
        for x in limit.split('~'):
            templist.append(str.strip(x.replace('cm',''))) # str.strip(공백을 없애길 원하는 단어)
        cmmin, cmmax = templist[0], templist[1]
    elif '이상' in limit:
        cmmin = int(limit.split("cm")[0])
    
    return ridename, cmmin, cmmax

ridename, cmmin, cmmax = rideread(str(input('>>> ')))
print(f'놀이기구 이름 : {ridename}')
print(f'최소 키 : {cmmin}cm')
print(f'최대 키 : {cmmax}cm')


