# a=1234*4
# b=1234/4

# if a>b :
#     print('a')
# else:
#     print('b')


# c = 15*5
# d = 15+15+15+15+15

# if c>d:
#     print('c is greater than d')
# elif c==d:
#     print('c is equal to d')
# elif c<d:
#     print('c is less than d')
# else:
#     print('I don\'t know')
    
# a = 48
# b = 4

# if a%b==0:
#     print(f'{a}는 {b}로 나누어 떨어집니다.')
# elif a%b!=0:
#     print(f'{a}는 {b}로 나누어 떨어지지 않습니다.')

# max=10

# while True:
#     num=int(input())
#     if num > max:
#         print(num, 'is too big!')
#         break

# num=int(input())
# if num==3:
#     print('삼')
# elif num==2:
#     print('이')
# elif num==1:
#     print('일')
# else:
#     print('1 이상 3 이하의 정수 중 하나를 입력하세요.')

# age=int(input("당신의 만 나이는 몇 살입니까? "))
# year=2023-age
# print(f'출생연도 = {year}')
# if year >= 1997:
#     print('당신은 Z세대 입니다.')
# elif year >= 1981 and year <= 1996:
#     print('당신은 밀레니얼 세대입니다.')
# elif year >= 1946 and year <= 1964:
#     print('당신은 X세대 입니다.')
# elif year >= 1925 and year <= 1945:
#     print('당신은 침묵 세대입니다.')
# else:
#     print('당신은 가장 위대한 세대입니다.')

# num=int(input())
# result = str(num)

# if num >= 10000000:
#     result = str(num // 10000000)+'M'
# elif num >= 1000:
#     result = str(num // 1000)+'k'
# elif num >= 0:
#     pass

# print(result)

## 사용자로부터 입력 받은 정수를 계속 더하다가, 음수가 입력되면 중단

# index=0
# while True:
#     num=int(input('임의의 정수를 입력해주세요. '))
#     if num>=0:
#         index+=num
#         print(f'현재 총합은 {index}입니다. 계속 진행합니다.')
#     else:
#         print('음수를 입력하셨습니다. 종료합니다.')
#         break



## 사용자로부터 정수를 입력 받고 그 총합이 음수가 될 때 중단

# index=0
# while index>=0:
#     num=int(input('임의의 정수를 입력해주세요. '))
#     index+=num
#     if index>=0:
#         print(f'현재 총합은 {index}입니다. 계속 진행합니다.')
#     else:
#         print('총합이 음수가 되었습니다. 종료합니다.')
#         break


## 윤년 판별하기

# 1. 4로 나누어 떨어지는 해는 윤년으로 한다.
# year % 4 == 0

# 2. 4,100으로 나누어 떨어지는 해는 평년으로 한다.
# year % 4 == 0 and year % 100 == 0

# 3. 4, 100, 400으로 나누어 떨어지는 해는 윤년으로 둔다.
# year % 4 == 0 and year % 100 == 0 and year % 400 == 0

# year=int(input('판별하고 싶은 연수를 입력하세요. '))
# if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#     print(f'입력하신 {year}년은 윤년입니다.')
# elif year % 4 == 0 and year % 100 == 0:
#     print(f'입력하신 {year}년은 평년입니다.')
# elif year % 4 == 0:
#     print(f'입력하신 {year}년은 윤년입니다.')
# else:
#     print(f'입력하신 {year}년은 평년입니다.')

# s='banana'
# if 'a' in s:
#     if 'b' in 'banana':
#         print('banana에는 a도 있고 b도 있어요!')
        
# if 'a' in s and 'b' in s:
#     print('banana에는 a도 있고 b도 있어요!')
# a_in_s='a' in s
# print(a_in_s)

# c_in_s = 'c' in s 
# print(c_in_s)

# a=3
# b=0
# print((a*b) > 0 and (a/b) > 0)
# print((a/b) > 0 and (a*b) > 0)

# age=int(input("당신의 만 나이는 몇 살입니까? "))
# year=2023-age
# country=str(input("당신의 한국입니까?(y/n) "))

# if country=='y':
#     print(f'출생연도 = {year}')
#     if year >= 1997:
#         print('당신은 한국의 Z세대 입니다.')
#     elif year >= 1981 and year <= 1996:
#         print('당신은 한국의 밀레니얼 세대입니다.')
#     elif year >= 1964 and year <= 1980:
#         print('당신은 한국의 X세대 입니다.')    
#     elif year >= 1955 and year <= 1963:
#         print('당신은 한국의 베이비 부머세대 입니다.')
#     elif year >= 1925 and year <= 1954:
#         print('당신은 한국의 침묵 세대입니다.')
#     else:
#         print('당신은 한국의 가장 위대한 세대입니다.')
# elif country=='n':
#     print(f'출생연도 = {year}')
#     if year >= 1997:
#         print('당신은 미국의 Z세대 입니다.')
#     elif year >= 1981 and year <= 1996:
#         print('당신은 미국의 밀레니얼 세대입니다.')
#     elif year >= 1965 and year <= 1980:
#         print('당신은 미국의 X세대 입니다.')        
#     elif year >= 1946 and year <= 1964:
#         print('당신은 미국의 베이비 부머 세대입니다.')
#     elif year >= 1925 and year <= 1945:
#         print('당신은 미국의 침묵 세대입니다.')
#     else:
#         print('당신은 미국의 가장 위대한 세대입니다.')

# family = ['mother', 'father', 'gentleman']

# for x in family:
#     print(x,len(x))
    
# print(list(range(2,7)))

# for i in range(4,8):
#     print(i)

# a = [4,5,6,7]
# for i in a:
#     print(i)

# num=int(input("임의의 정수를 입력하세요. "))
  
# for i in range(num):
#     print(num)

# for i in range(num):
#     print(i+1, (i+1)*(i+1))

# L=input().split()

# min=int(L[0])
# max=int(L[1])
# print(f'최소 온도: {min}도')
# print(f'최대 온도: {max}도')

# temp = int(input())

# while temp != 999:
#     if min <= temp <= max:
#         print('Nothing to report')
#         temp = int(input())
#     else:
#         print('Alert!!')
#         break

# for n in range(1,11):
#     match n%2:
#         case 0:
#             print(f"{n} is even.")
#         case 1:
#             print(f"{n} is odd.")
            
## Fizzbuzz for + if
# for i in range(1,101):
#     if i%3==0 and i%5!=0 :
#         print(i,'\tFizz!!')
#     elif i%5==0 and i%3!=0:
#         print(i,'\tBuzz!!')
#     elif i%3==0 and i%5==0:
#         print(i,'\tFizzbuzz!!')
#     else:
#         print(i)

## Fizzbuzz for + match-case
# for i in range(1,101):
#     match (i%3,i%5):
#         case (0,_):
#             print(i,'\tFizz!!')
#         case (_,0):
#             print(i,'\tBuzz!!')
#         case (0,0):
#             print(i,'\tFizzbuzz!!')
#         case _:
#             print(i)

# for x in [1,2,3,4]:
#     if x%3:
#         print(x)
#     else:
#         break
# else:
#     print("리스트의 원소를 모두 출력했어요.")

# countdown=5
# while countdown>0:
#     print(countdown)
#     countdown-=1
#     if input()=='중단':
#         break
# else:
#     print('Fire!!!')






