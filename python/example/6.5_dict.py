## dict 자료형
# 키 밸류 방식

dic={} # dict 자료형을 정의한다.
dic['dictionary'] = '. A referenc book ...'
dic['pytyhon'] = 'Any of various nonvenomus snakes of the...'
print(dic['dictionary'])


smalldic = {'dictionary': 'reference', 'python': 'snake'}
print(smalldic['python'])

# dict 속성 제거하기
print(smalldic)
del smalldic['dictionary']
print(smalldic)
smalldic['dictionary'] = 'reference'
print(smalldic)

family={'mom':'Choi','dad':'Hong','son':'Hong'}
print(family)
# 해당 dict의 키 확인하기
print(family.keys())

# 해당 dict의 값 확인하기
print(family.values())

# 해당 키의 값 확인하기
print(family['mom'])

# 해당 dict의 키와 값 모두 확인하기
print(family.items())

# 해당 키가 dcit에 있는지 확인
print('dad' in family)
print('sister' in family)

## 연습문제
# 
# def korean_number(num):
#     d = {0: '영', 1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
#     return d[num]

# print(korean_number(2))

def Korean_number(x):
    num={0:'영',1:'일'}
    return num[x]
    
print(Korean_number(0))

# 사자성어 사전 만들기

# Saja={
#         '江湖之樂(강호지락)': '자연을 벗 삼아 누리는 즐거움',
#     '欲速不達(욕속부달)': '빨리 하고자 하면 이루지 못함',
#     '積小成大(적소성대)': '작은 것을 쌓아 큰 것을 이룸',
#     '勤儉節約(근검절약)': '부지런하고 알뜰하게 재물을 아낌',
#     '經世濟民(경세제민)': '세상을 다스리고 백성을 구제함',
#     '塞翁之馬(새옹지마)': '인생의 길흉화복은 변화가 많아서 예측하기가 어려움',
#     '好事多魔(호사다마)': '좋은 일에는 흔히 방해되는 일이 많음',
#     '桑田碧海(상전벽해)': '세상일의 변천이 심함',
#     '自業自得(자업자득)': '자기가 저지른 일의 결과를 자기가 받음',
#     '因果應報(인과응보)': '원인과 결과가 상응하여 보답한다',
#     '愚公移山(우공이산)': '어떤 일이든 끊임없이 노력하면 반드시 이루어짐',
# }
# for x,y in Saja.items():
#     input('Enter를 누르세요!')
#     print(f'{x}\n{y}')

## 질환 dic 만들기
# txt = '''신경발달장애 Neurodevelopmental Disorders
# 조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
# 양극성 및 관련 장애 Bipolar and Related Disorders
# 우울장애 Depressive Disorders
# 불안장애 Anxiety Disorder
# 강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
# 외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
# 해리장애 Dissociative Disorders
# 신체증상 및 관련 장애 Somatic Symptom and Related Disorders
# 급식 및 섭식장애 Feeding and Eating Disorders
# 배설장애 Elimination Disorders
# 수면－각성 장애 Sleep－Wake Disorders
# 성기능부전 Sexual Dysfunctions
# 성별 불쾌감 Gender Dysphoria
# 파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
# 물질관련 및 중독 장애 Substance－Related and Addictive Disorders
# 신경인지장애 Neurocognitive Disorders
# 성격장애 Personality Disorders
# 변태성욕장애 Paraphilic Disorders
# 기타 정신질환 Other Mental Disorders'''

# disorders = dict()

# # 해당 함수를 이용하여 영어의 등장을 구분한다. (유니코드로 식별)
# ord() 함수로 해당 문자의 유니코드를 받환할 수 있다.
# is_eng = lambda x: 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122
# print('A부터 Z까지 ',ord('A'),'~',ord('Z'))
# print('a부터 z까지 ',ord('a'),'~',ord('z'))

# # txt를 엔터 기준으로 짤라서
# for l in txt.splitlines():
#     i = 0
#     while not is_eng(l[i]):
#         i += 1
#     else:
#         ko, en = l[:i - 1], l[i:]
#         print(f'영단어로 시작하는 번호는 {i} {l[i:]}')
#         disorders[ko] = en               











txt = '''신경발달장애 Neurodevelopmental Disorders
조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
양극성 및 관련 장애 Bipolar and Related Disorders
우울장애 Depressive Disorders
불안장애 Anxiety Disorder
강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
해리장애 Dissociative Disorders'''

# disorder=dict()
# print(ord('A'),ord('Z'))
# print(ord('a'),ord('z'))

# start_english = lambda x : 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122

# for i in txt.splitlines():
#     j=0
#     while not start_english(i[j]):
#         j+=1
#     else:
#         kor, en = i[0:j-1], i[j:]
#         disorder[kor]=en

# print(disorder)
       
# 프랙털?

# colwidth = 61
# rule90 = {'000':'0', '001':'1', '010':'0', '011':'1', '100':'1', '101':'0', '110':'1', '111':'0'}

# half = colwidth // 2
# line = '0' * half + '1' + '0' * half
# print(line)

# while line[1] == '0':
#     prev = line
#     line = '0' * colwidth
#     for i in range(1, colwidth - 1):
#         line = line[:i] + rule90[prev[i-1:i+2]] + line[i+1:]
#     print(line)
    

# width = 121
# rule = {'111':'0', '110':'1', '101':'0', '100':'1', '011':'1', '010':'0', '001':'1', '000':'0'}

# half = width//2
# line = '0' * half + '1' + '0' * half
# print(line)

# while line[1] == '0':
#     preline=line
#     line = '0' * width
#     for i in range(1,width-1):
#         # print(f'i = {i}\npreline = {preline[i-1:i+2]} -> rule = {rule[preline[i-1:i+2]]}')
#         line = line[:i] + rule[preline[i-1:i+2]] + line[i+1:]
#         # 라인 i=1 부터 계속 유지되면서 이전 줄을 참고해 규칙에 해당되는 값을 바꿔준다.
#     print(line)
    
    




    
    












