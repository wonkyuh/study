# 성적표 만들기
# wonkyo = [80,90,85]
# namtaek = [90,80,88]
# taehan = [80,95,85]
# minseok = [95,85,80]

# students = [wonkyo, namtaek, taehan, minseok]

# for scores in students:
#     print(scores)

# for scores in students:
#     print(f'{scores=}')
#     print('합계는 ',sum(scores))
#     print('평균은 ',sum(scores)/3)

# 문자열 슬라이싱
# p = 'Python'
# print(p[:2])
# h = 'Hello world!'
# print(h[:6] + p + '!')
# print(h[:6] + p + h[-1:])
# print(h.replace('world','Python'))
# print(h[:])
# print(p[::-1])

# 리스트 슬라이싱
# N = [1,2,3,4,5,6,7,8,9,10]
# print(N[0])
# print(N[:5])
# print(N[5:])
# print(N[-5:])
# print(N[:-5])
# print(N[::-1])
# print(N[::-2])

# fruit=['apple','banana','cherry', 'mango', 'orange']      
# print(fruit[0:2])
# print(fruit[2])

# 회문 판별 함수
# 회문이란? 거꾸로 배열해도 같은 단어를 말한다.

## 내 정답
# def palindrome(x):
#     x=x.lower().replace(' ','')
#     plus=1
#     minus=0
#     result = 0
#     if len(x)%2==0:
#         for i in x:
#             if i == x[len(x)-plus]:
#                 # print(f'{plus}번째 글자와 {len(x)+minus}번째 글자와 같다.')
#                 result += 1
#                 if plus == len(x)/2:
#                     break
#             else:
#                 # print(f'{plus}번째 글자와 {len(x)+minus}번째 글자와 같지 않다.')
#                 if plus == len(x)/2:
#                     break
#             plus+= 1
#             minus-=1
#         if result == len(x)/2:
#             print(f'{x}는 회문입니다.')    
#         else:
#             print(f'{x}는 회문이 아닙니다.')            
#     else:
#         for i in x:
#             if i == x[len(x)-plus]:
#                 # print(f'{plus}번째 글자와 {len(x)+minus}번째 글자와 같다.')
#                 result += 1
#                 if plus==int(len(x)/2)+1:
#                     break
#             else:
#                 # print(f'{plus}번째 글자와 {len(x)+minus}번째 글자와 같지 않다.')
#                 if plus == len(x)/2:
#                     break
#             plus+= 1
#             minus-=1
#         if result == (int(len(x)/2))+1 :
#             print(f'{x}는 회문입니다.')    
#         else:
#             print(f'{x}는 회문이 아닙니다.')


# palindrome('annA')
# palindrome('banana')
# palindrome('Level')
# palindrome('My gym')

## 강사님 정답
# def palin(s):
#     s=s.lower().replace(' ','')
#     return s[:] == s[::-1] # Treu 혹은 False로 리턴

# if __name__ == '__main__':
#     for x in ['annA', 'banana', 'Level', 'My gym']:
#         if palin(x):
#             print(f"'{x}' is a panlindrome")
#         else:
#             print(f"'{x}' is not a palindrome")

## 강사님 정답보고 내 정답 수정해보기
# def palindrome(x):
#     x=x.lower().replace(' ','')
#     plus=1
#     minus=0
#     result = 0
#     if len(x)%2==0:
#         for i in x:
#             if i == x[len(x)-plus]:
#                 result += 1
#                 if plus == len(x)/2:
#                     break
#             else:
#                 if plus == len(x)/2:
#                     break
#             plus+= 1
#             minus-=1
#         return result == len(x)/2
#     else:
#         for i in x:
#             if i == x[len(x)-plus]:
#                 result += 1
#                 if plus==int(len(x)/2)+1:
#                     break
#             else:
#                 if plus == len(x)/2:
#                     break
#             plus+= 1
#             minus-=1
#         return result == (int(len(x)/2))+1
        
# if __name__ == '__main__':
#     for x in ['annA', 'banana', 'Level', 'My gym']:
#         if palindrome(x):
#             print(f"'{x}'은/는 회문입니다.")
#         else:
#             print(f"'{x}'은/는 회문이 아닙니다.")
            
## 강사님 스타일로 다시 만들어보기
# def pal(x):
#     x=x.lower().replace(' ','')
#     return x==x[::-1]
# if __name__=='__main__':
#     for s in ['annA', 'banana', 'Level', 'My gym']:
#         if pal(s):
#             print(f'{s}는 회문')
#         else:
#             print(f'{s}는 회문아님')

## 각 자리 숫자의 합을 구하는 함수(리스트를 이용)

# def sumsum(x):
#     x=str(x)
#     y=[]
#     for i in x:
#         y.append(i)
#     y=list(map(int,y))
#     print(sum(y))
    
# sumsum(123)

## 파이썬 숫자 각 자리수를 원소 삼아 리스트로 변환
# s=1234
# s=list(map(int,str(s)))
# print(s)

## 위 함수를 이용하여 더 간단히 만들기
# def sumsum2(x):
#     x=list(map(int,str(x)))
#     print(sum(x))
    
# sumsum2(123)

## 줄기와 잎 형식 리스트 만들기
# score = [0,0,2,4,7,7,9]
# score += [11,11,13,18]
# score += [20]

# stem_leaf=[[], [], []]
# def sl_function(x):
#     for i in x:
#         if int(i/10) == 0:
#             stem_leaf[0].append(i)
#         elif int(i/10) == 1:    
#             stem_leaf[1].append(i%10)
#         elif int(i/10) == 2:    
#             stem_leaf[2].append(i%10)
#     print(f'0: {stem_leaf[0]}')
#     print(f'1: {stem_leaf[1]}')
#     print(f'2: {stem_leaf[2]}')
    
# sl_function(score)

## divmod 함수
# 두 인자를 나눠 몫과 나머지를 반환한다.
# score = [0,0,2,4,7,7,9]
# score += [11,11,13,18]
# score += [20]

# stem_leaf=[[], [], []]
# for s in score:
#     d, m = divmod(s, 10)
#     stem_leaf[d].append(m)
# for i in range(len(stem_leaf)):
#     print(f'{i}: {stem_leaf[i]}')
    
## 각 자리 숫자의 합을 구하는 함수 map() 이용
# def sumOfDigits(x):
#     num=list(map(int,x))
#     print(f'만들어진 리스트 : {num}')
#     return sum(num)

# num=input()
# print(sumOfDigits(num))

## 소수 구하기
# 1 혹은 자기 자신만 갖는 수

# def sosu(x):
#     L=list(range(2,x+1))
#     for j in L :
#         print(f'j = {j}')
#         for i in L:
#             print(f'\t\t\ti = {i}')
#             if i>j and i % j == 0:
#                 L.remove(i)
#                 print(f'\t\t\t{i}>{j} and {i} % {j} == 0 을 만족하므로 삭제한다.')
#     print(L)

# sosu(25)

## 진법 변환
# def sipjinsu(x):
#     init=''
#     x1=x
#     print(f'{x1} ÷ 2 =',int(x/2),' 나머지는 ',x1%2)
#     while x/2 > 0 :
#         init+=(str(x1%2))
#         x1=int(x1/2)
#         if x1 == 0 :
#             break
#         print(f'{x1} ÷ 2 = ',int(x1/2),' 나머지는 ',x1%2)
#     init=init[::-1]
#     print(f'십진수인 {x}를 이진수로 변환하면 {init}이다.')
    
# sipjinsu(31)