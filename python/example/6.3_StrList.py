# # 문자열
# x = 'banana'
# print(x[0])
# print(x[0:4])
# print(x[:4])
# print(x[4:])

# s = ' hello Python! '
# 문자열에서 특정 문자 검색
# print(s.find('P'))
# y = s[0:6]
# print(y)

# 공백 제거
# print(y.strip()) # 앞뒤 공백 제거
# print(y.rstrip()) # 뒤 공백 제거

# 문자열 쪼개서 리스트 담기
# print(s.split())
# print(s.split()[0])

# prime = [3,7,11]
# print(prime)

# 리스트 원소 추가
# prime.append(5) # 리스트 원소 추가
# print(prime)

# 리스트 정렬
# prime.sort() # 리스트 오름차순 정렬
# print(prime)

# 특정 위치에 특정 원소 추가하기
# prime.insert(0,2) # 리스트 맨 앞(0)에 원소(2) 추가
# print(prime)
# prime.insert(2,4)  # Test
# print(prime) # Good

# 특정 위치 원소 지우기
# del prime[5]
# print(prime)

# 특정 위치 원소 삭제하면서 변수로 정의하기
# n = prime.pop(3)
# print(prime)
# print(n)

# 리스트 안에 리스트 넣기
# orders = ['popato',['pizza','Coke','salad'],'hamburger']
# print(orders[1])
# print(orders[1][1])

# 문자열을 리스트에 넣어보기
# characters=[]
# sentence='Be happy'
# for char in sentence:
#     characters.append(char)
# print(characters)

# 숫자를 문자열로 바꾸기
# my_int = 123
# print (type(my_int))
# my_int = str(my_int)
# print (type(my_int))

# 문자열 숫자로 바꾸기
# type(int('123'))
# type(float('123'))

# 리스트 원소들의 합 구하기
# one_to_ten = list(range(1,11))
# print(one_to_ten)
# print(sum(one_to_ten)) # sum()를 이용한 리스트 원소 합
