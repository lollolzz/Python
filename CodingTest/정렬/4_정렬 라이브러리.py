"""
날짜 : 21/09/03
이름 : 권능한
내용 : 코딩테스트 - 파이썬 정렬 라이브러리 실습

"""



array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted : 퀵정렬을 기반으로 설계된 파이썬 정렬 함수
result1 = sorted(array)
print('result :', result1)

result2 = sorted(array, reverse=True)
print('result2 :', result2)


# sort : 파이썬 리스트 정렬 멤버 함수
array.sort()
print('array1 :', array)

array.sort(reverse=True)
print('array2 :', array)

#key 매개변수의 활용
dataset = [['바나나', 2], ['사과',5], ['당근',3]]

def setting(data):
    return data[1]

ds1 = sorted(dataset, key=setting)
print('ds1 :', ds1)

ds2 = sorted(dataset, key=lambda data:data[1])
print('ds2 :', ds2)