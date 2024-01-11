def rideread(text):
    ridename, limit = map(str.strip, text.split(':')) 
    # 입력 받은 text를 : 기준으로 나누어 리스트에 담기 전에
    # str.strip을 통해 앞뒤 공백을 제거하고 담는다.
    
    cmmin=cmmax=None # 변수를 정의하고
    if '~' in limit: # 만약 ~가 limit 값에 포함되어 있다면
        templist=[]
        for x in limit.split('~'): # ~ 기준으로 나뉜 리스트를 for반복하여
            templist.append(x.replace('cm','')) # cm를 제거한 값을 templist에 추가한다.
        cmmin, cmmax = int(templist[0]), int(templist[1]) # 그래서 templist의 [0], [1]을 각각 변수로 정의한다.
    elif '이상' in limit: # 만약 이상이 limit 값에 포함되어 있다면 
        cmmin = int(limit.split("cm")[0]) # cm

    return ridename, cmmin, cmmax