## 파일 열기
# f = open("C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\Fun.txt")
# print(f.read())

## 파일 쓰기 모드로 열기 ('w')
# f = open("C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\Fun2.txt",'w')
# f.write('FunFun!')
# f.close()

## 파일 추가 모드로 열기 ('a')
# f = open("C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\Fun.txt",'a')
# f.write('\nFunFunFun!')
# f.close()

## 파일 한 줄씩 출력 readline
# f = open("C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\Fun.txt")
# for x in range(6):
#     print(f.readline())
    
## 파일 한 줄씩 리스트에 담아 출력 readlines
# f = open("C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\Fun.txt")
# line = f.readlines()
# # print(line)
# # print(line[:3])
# for i in line[0:3]:
#     print(i,end='')

## 연습문제

## 밴드 이름 만들기
# color = open("C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\color.txt")
# food = open("C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\food.txt")

# with open('C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\color.txt', 'r', encoding='utf-8') as color:
#     cline = color.readlines()
# with open('C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\food.txt', 'r', encoding='utf-8') as food:
#     fline = food.readlines()

# import random
# x=random.choice(cline).strip()
# y=random.choice(fline).strip()
# print(f'{x} {y}')

## 기밀문서 해독하기
# with open('C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\doc.txt', 'r', encoding='utf-8') as doc:
#     docline = doc.readlines()

# for i in docline[3:9]:
#     print(i,end='')
    
# for j in docline[3:9]:
#     j=j.replace(':','')
#     j=j.replace('.','')
#     j=j.replace(',','')
#     j=j.upper()
#     i=j.split()
#     for i in i[:2]: # 앞 두 단어만 따서 문장 만들기
#         print(i,end=' ')

## 영어 문장 테스트
# with open('C:\\Users\\USER\\Desktop\\git\\study\\python\\example\\text\\entest.txt', 'r', encoding='utf-8') as entest:
#     entestline = entest.readlines()

# for i in entestline[0:len(entestline)]:
#     L=i.replace('\n','').split('\t')
#     print('해당 문장을 영어로 작성해보세요!\n')
#     print(L[0])
#     A=input()
#     if A==L[1]:
#         print('Correct!')
#     else:
#         print('Not correct')
#     print('-----------------------------------')



