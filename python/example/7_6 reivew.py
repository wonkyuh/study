## complex
# 복소수는 실수와 허수의 조합
# 4+1j 일 경우 4가 실수 1j가 허수

# i^2 = -1이 되는 수를 허수라고 한다.
# 이런 경우가 있나..?

## Sequence
# 문자열, 리스트, 튜플, 사용자 정의 클래스가 시퀀스다.
print(type(['love', 'enemy',]))

## Mapping
# 키-밸류의 딕셔너리 타입을 매핑이라고 한다.

## bool
# 참, 거짓
# print(type(True))
# print(type(3>1))

## set는 집합을 의미한다.
# 집합을 표현한다.
# fruits = {'apple','banana','orange'}
# print(type(fruits))

## 성적표 만들기
# wonkyo = [80,90,85]
# namtaek = [90,80,88]
# taehan = [80,95,85]
# minseok = [95,85,80]
# stName = ['wonkyo','namtaek','taehan','minseok']
# student = [wonkyo, namtaek, taehan, minseok]
# print(type(student))
# i=0
# for scores in student:
#     print(f'{stName[i]}의 성적표')
#     print(f'수학 점수 = {scores[0]}')
#     print(f'과학 점수 = {scores[1]}')
#     print(f'국어 점수 = {scores[2]}')
#     i+=1
    
# p = 'Python'
# print(p[:2])
# h = 'Hello world'
# Hello
# print(h[:6])
# print(h[:-6])

# world
# print(h[6:11])
# print(h[-5:])

# 띄엄띄엄 슬라이싱 (규칙)
# N=[1,2,3,4,5,6,7,8,9,10]

# 인덱스 0부터 +2씩만 출력
# print(N[::2])

# 인덱스 0부터 +3씩만 출력
# print(N[::3])

# 문자열 포맷팅(형식화)
# https://datascienceschool.net/01%20python/02.04%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98%20%EB%AC%B8%EC%9E%90%EC%97%B4%20%ED%98%95%EC%8B%9D%ED%99%94.html
# price=5.89
# print(('가격은 %3d만원입니다.')% price)

## 회문 판별 함수
# 거꾸로 배열해도 같은 단어인 것

# def PAND(text):
#     text=list(str(text.lower()))
#     num=len(text)
#     # 입력된 텍스트가 홀수면 정가운데 문자를 리스트에서 제거
#     if num%2==0:
#         pass
#     elif num%2!=0:
#         print('인덱스 ',(num//2+1)-1,'번을 제거합니다.')
#         del text[(num//2+1)-1]
    
#     # 회문 검사 시작
#     print(f'회문을 검사 시작합니다. {text}')
#     num=len(text)
#     for i in range(0,int(round(num/2,0))): # range의 len을 num으로 바꿔도 될까?
#         if text[i]==text[num-1]:
#             pass
#             print(f'{text[i]} = {text[num-1]} 이므로')
#             print(f'{i+1}차 통과 성공')

#         elif text[i]!=text[num-1]:
#             print(f'{text[i]} != {text[num-1]} 이므로')
#             print('회문이 아닙니다.')
#             break
#         num-=1
#     else:
#         print('회문이 맞습니다.')
        
    
# PAND('NgNgn')


    
# def sumall(x):
#     x=list(str(x))
#     sum=0
#     for i in x:
#         sum+=int(i)
#     print(sum)
    
# sumall(456)

## 소수구하기
# 1 혹은 자기 자신만 갖는 숫자

# def sosu(x):
#     sosu_list=[2,3,5,7,11]
#     for i in range(8,x):        
#         if i%2!=0:
#             if i%3!=0:
#                 if i%5!=0:
#                     if i%7!=0:
#                         if i%11!=0:
#                             sosu_list.append(i)
                            
#     print(sosu_list)    
# ## 8 이상부터 
# x=150
# sosu(x)

# def sosu(x):
#     L=list(range(2,x+1))
#     for j in L:
#         for i in L:
#             if i>j and i%j==0:
#                 L.remove(i)
#     print(L)

# sosu(25)    

# # 문자열에서 특정 문자 검색
# s = ' hello Python! '
# print(s.find('P'))

# # 앞뒤 공백 제거 # 뒤 공백 제거는 rstrip
# print(s)
# print(s.strip())

# # 특정 위치에 문자열 추가하기
# prime=[1,2,3,5,6]
# prime.insert(3,4) # 인덱스 3번에 '4'를 추가한다.
# print(prime)

# # 특정 위치 문자열 지우기
# del prime[5]
# print(prime)

# # 특정 위치 문자열 제거하면서 변수로 뽑아내기
# n=prime.pop(4)
# print(prime)
# print(f'n = {n}')

# # 문자열을 리스트에 넣어보기
# characters=[]
# sentences='Be happy'
# for char in sentences:
#     characters.append(char)
# print(characters)

# # 문자열은 이렇게만 해도 된다 ㅎ
# print(list(sentences))

# # 리스트 원소들의 합 구하기
# LLL = [1,2,3,4,5]
# print(sum(LLL))

# list = [] , tuple = () 튜플은 괄호가 필요 없다. 쉼표만 
## tuple
# 튜플이란?
# 여러 자료형을 담을 수 있으면서
# 절대 변하지 않는 자료형을 말한다.
# 변경, 추가, 삭제 그 어떤 것도 할 수 없다.
c, d = 10, 20
c, d = d, c

print(c,d)
# 파이썬은 간편하게 변수를 서로 바꿀 수 있다.

# 나머지를 튜플로 묶는다?
# def magu_print(x,y,z,*rest):
#     print(x,y,z,rest)
#     print(type(rest))

# magu_print(1,2,3,4,5,6,7,8,9)

# t=('a','b','c')
# print(t)
# empty=()
# print(empty)
# one = 5,
# print(one)

# 날짜 튜플로 받기
# def read_date():
#     year, month, day = tuple (map(int, input().split()))
#     return year, month, day

# year, month, day = read_date()
# print('%02d/%02d/%04d'%(month,day,year))

# list = [], tuple = (), dict = {'key':'value'}
## dic 자료형
# dic = {}
# dic['dictionary'] = 'A reference book..'
# dic['python'] = 'Any of various..'
# print(dic['dictionary'])
# print(dic['python'])

# smalldic={'dictionary':'reference','python':'snake'}
# print(smalldic['python'])

## 키와 값들을 출력하기
# print(smalldic.keys())
# print(smalldic.values ())

## 키, 값 한번에 출력하는 items를 이용하기
# for x,y in smalldic.items():
#     input('Enter를 누르세요!')
#     print(f'{x}\n{y}')

# list = [], tuple = (), dict = {'key':'value'}
# set = {}

## Set 집합
# fruits={'apple','banana','orange'}
# fruits.add('mango')
# print(fruits)

