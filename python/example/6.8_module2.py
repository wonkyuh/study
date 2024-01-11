## sys 모듈
# import sys
# sys.ps1
# sys.ps1 = '^^; '
# 

## os 모듈
# import os
# os.getcwd()
# os.listdir()
# os.chdir()

## random
# import random
# print(random.random())

# # 1 ~ 10까지
# print(round(10*random.random()))
# print(random.randrange(1,11))

# a=list(range(1,7))

# print(a)
# print(type(a))
# random.shuffle(a) # shuffle 함수는 섞어주고 return 값이 따로 없다.
# print(a)

# b=['a','b','c','d','e','f']
# random.shuffle(b)
# print(b)

# menu='쫄면','육계장','비빔밥'
# print(random.choice(menu))

## 연습문제
# 밴드 이름 짓기
# import random

# color=['검은','하얀','파란','갈색']
# name=['콰삭칩','소보로','쭈꾸미','커피','옹심이']
# random.shuffle(color)
# random.shuffle(name)
# for i,j in zip(color,name): # zip 함수로 두 개의 데이터를 엮을 수 있다.
#     print(i,j)

# string과 random 모듈을 이용해 비밀번호 생성
# string 모듈
# import string , random
# string.ascii_uppercase # 대문자
# string.ascii_lowercase # 소문자
# string.ascii_letters # 대소문자 모두
# string.digits # 숫자 (0 ~ 9)

# alphanumeric= string.ascii_letters + string.digits
# alphanumeric=set(alphanumeric)-set('lI0O')
# alphanumeric.update('@','#','$','%')
# alphanumeric=list(alphanumeric)

# print(random.choice(alphanumeric))
# pw=''
# for i in range(12):
#     pw+=random.choice(alphanumeric)

# print(pw)

# 숫자, 소문자, 대문자 1개 이상, 특수문자 1개 이상 포함한 비밀번호 생성기 
import string, random

upper=string.ascii_uppercase
special='!','@','#','$','%','_'
lower=string.ascii_lowercase
num=string.digits

U=random.randrange(1,7) # 최소 한자리 ~ 최대 6자리
S=random.randrange(1,5) # 최소 한자리 ~ 최대 4자리
len=12
lowerrandrange=range(0,U)
digitsrandrange=range(0,S)

pw=''

for j in lowerrandrange:
    pw+=random.choice(lower)
    len-=1
     
for p in digitsrandrange:
    pw+=random.choice(num)
    len-=1

for i in range(0,(random.randrange(1,len))):
    pw+=random.choice(upper)
    len-=1

for i in range(0,len):
    pw+=random.choice(special)
    len-=1
   
pw=list(pw)
random.shuffle(pw)
pw=''.join(pw)
print(f'생성된 비밀번호는 {pw} 입니다.')

## 시저 암호 만들기
import string

aa=string.ascii_lowercase
AA=string.ascii_uppercase[3:]+string.ascii_uppercase[:3]

# maketrans로 두 개의 데이터 dict으로 엮기
tt=str.maketrans(aa, AA) # aa = keys, AA = values
print(type(tt))
print('traue nie dem brutus'.translate(tt))

