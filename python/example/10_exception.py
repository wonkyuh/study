## 예외처리 (try, except)

def f(a,b):
    return (a*b) + (a/b)

print(f(1,2))
# b가 0 일 때 오류가 발생하므로
# 예외처리를 진행해준다.

def e(a,b):
    try:
        if a and b:
            return (a*b) + (a/b)
        elif a:
            return '불능'
        else:
            return '부정'
    except:
        return '똑바로 살아라'
print(e('이십','오'))
