
# ## math 모듈
# import math
# print(math.sqrt(2))
# print(math.sqrt(3))
# print(math.sqrt(4))

# print(math.pi)

# ## calendar 모듈
# import calendar
# calendar.prmonth(2023,12)

# ## tkinter 모듈 (작동 안됨)
# from tkinter import *
# widget = Label(None,text='I love myself!')
# widget.pack()

# # tkinter 모듈의 Label이 되어버림
# print(Label)

# del Label
# # print(Label)

# print(dir(calendar))
# print([x for x in dir(calendar) if 'leap' in x])

# print(help(calendar.isleap))

# print(calendar.isleap(2077))

# ## 연습문제
# # 직각삼각형의 빗변 길이 구하기
# def hypotenuse(x,y):
#     c=math.sqrt(x**2 + y**2)
#     return round(c,2) # 소수점 자리수에 맞춰 반올림
    
# print(hypotenuse(10,20))

# # Calendar
# c = calendar.TextCalendar()
# m = c.prmonth(2021,2)


# 놀이 공원 1
# 본인의 키를 입력하여 탈 수 있는 놀이기구 조회하기
# import sys

# sys.path.append("./")
# import ridereader

# rides = '''와일드 윙: 110cm 이상
# 드림보트: 120cm 이상
# 자이안트 루프: 120cm 이상
# 툼 오브 호러: -
# 플라이벤처: 140cm~195cm
# 회전목마: 100cm 이상
# 매직 붕붕카: 110cm~140cm'''



# def allowedrides(height):
#     assert type(height) == int

#     result = [] 
    
#     for i in rides.splitlines():
#         ridename, cmmin, cmmax = ridereader.rideread(i)
#         if (not cmmin and not cmmax) or (height >= cmmin and not cmmax) or (cmmin <= height <= cmmax):
#             result.append(ridename)
        
#     return result


# if __name__ == "__main__":
#     height = int(input())
#     print(allowedrides(height))

# 놀이 공원 2
# 세명이 같이 탈 수 있는 놀이 기구 조회하기
import sys

sys.path.append("./")
import ridereader

rides = '''와일드 윙: 110cm 이상
드림보트: 120cm 이상
자이안트 루프: 120cm 이상
툼 오브 호러: -
플라이벤처: 140cm~195cm
회전목마: 100cm 이상
매직 붕붕카: 110cm~140cm'''



def allowedrides(height):
    assert type(height) == int

    result = [] 
    
    for i in rides.splitlines():
        ridename, cmmin, cmmax = ridereader.rideread(i)
        if (not cmmin and not cmmax) or (height >= cmmin and not cmmax) or (cmmin <= height <= cmmax):
            result.append(ridename)
        
    return result


if __name__ == "__main__":
    height1, height2, height3 = int(input()), int(input()), int(input())
    set1=set(allowedrides(height1))
    set2=set(allowedrides(height2))
    set3=set(allowedrides(height3))
    # set3=set(allowedrides(height1))
    print(set1&set2&set3)
