
# ## Set {집합}

# fruits = {'apple','banana','orange'}
# fruits.add('mango')
# print(fruits)

# companies = set()
# companies = {'apple','microsoft','google'}

# print(type(fruits))
# print(type(companies))

# # 교집합(&) 합집합(|)
# print(fruits & companies)
# print(fruits | companies)

# # 여러 세트를 리스트에 담아서 set 메서드를 사용할 수도 있다.
# list_of_sets = [fruits, companies]
# print(set.intersection(*list_of_sets))
# print(set.union(*list_of_sets))

# # list -> set 중복 원소를 갖지 않는다.
# alphabet = list('google')
# print(alphabet)
# print(set(alphabet))

# # Set(집합)끼리는 뺄셈도 가능하다.
# S1 = {1,2,3,4,5,6,7}
# S2 = {2,4,6}
# print(S1-S2)

# ## 연습 문제
# # 주사위의 합을 구하시오. (단, 같은 숫자는 한번만 출력합니다.)
# dice1 = (1, 2, 3, 4, 5, 6)
# dice2 = (2, 3, 5, 7, 11, 13)
# sum = set()

# for i in dice1:
#     for j in dice2:
#         sum.add(i+j)
        
# print(sum)

# 끝말 잇기;;
all=set()
DanAeo=set()
DanAeo={'게맛살','구멍','글라이더','기차','대롱','더치페이',
    '롱다리','리본','멍게','박쥐','본네트','빨대','살구',
    '양심','이빨','이자','자율','주기','쥐구멍','차박',
    '트라이앵글','본드','기러기','대기','심박'}

print('<시작>끝말잇기를 하자. 내가 먼저 말할게.\n기차')
all.add('기차')
DanAeo.remove('기차')
ex='기차'
answer=''
trigger=0

while trigger==0:
    print(all)
    answer=input('> ')
    if ex[-1]!=answer[0]:
        print('글자가 안 이어져. 내가 이겼다!<끝>')
        trigger=1
        break
    elif answer in all:
        print('아까 했던 말이야. 내가 이겼어!<끝>')
        trigger=1
        break
    for i in all:
        if i!=answer:
            for j in set(DanAeo):
                if answer[-1] == j[0]:
                    print(j)
                    DanAeo.remove(j)
                    all.add(j)
                    all.add(answer)                    
                    ex=j
                    break
            else:
                print('졌다!<끝>')
                trigger=1
                break
            break
