print(type('egoing'))
name = 'egoing'
print(name)
print(type(['egoing', 'leezche', 'graphittie']))
# 문자열들이 하나로 뭉쳐져서 list라는 데이터 type이 됨
# [] - list, () - tuple, {} - dict
names = ['egoing', 'leezche', 'graphittie']
# list를 하나의 변수에 담음
print(names)
# index란 각각의 데이터들이 데이터에 저장 될 때 각각의 데이터들이 가지는 번호,
# 즉 식별자라고도 함
print(names[1])
egoing = ['programmer', 'seoul', 33, True]
# 하나의 list에는 다양한 형태의 데이터 타입이 들어갈 수 있다
egoing[1] = 'busan'
print(egoing)