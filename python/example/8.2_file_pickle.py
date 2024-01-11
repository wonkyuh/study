## pickle
# import pickle

# users={'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
# f = open('users','wb') # byte형식으로 쓰겠다.
# pickle.dump(users,f) # 파이썬 경로에 user 라는 이름으로 파일 백업
# f.close()

# f = open('users','rb') # byte형식으로 읽겠다.
# a = pickle.load(f)
# print(a)

## glob
# 파일들의 리스트를 뽑는데 사용하는 모듈

# from glob import glob
# print(glob('.\study\python\example\*.py'))
# print(glob(r'c:\U*')) # 앞에 r 표시는 원시(raw) 문자열을 사용하는 것

## os.path
# glob와 os.path 모듈을 사용한 예제

# from glob import glob
# from os.path import isdir

## isdir은 디렉토리인지 아닌지 참거짓을 판별하는 모듈

# for x in glob('/*'):
#     if isdir(x):
#         print(x, '<DIR>')
#     else: print(x)

## 애국가 합치기
from glob import glob

Anthem = glob('.\\study\\python\\example\\text\\kor_*')
n=1
AllAnthem = ''
with open('AllAnthem','wt',encoding='utf-8') as f : # wt = 텍스트 모드로 쓰기 모드 오픈
   for i in Anthem:
      with open(i, 'r', encoding='utf-8') as i:
         f.write(f'{n}절\n'+i.read()+'\n\n')
      n+=1
f.close()



   
    
