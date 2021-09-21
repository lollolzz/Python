"""
날짜 : 2021/09/17
이름 : 권능한
내용 : 코딩테스트 - 이진탐색 라이브러리

"""
# 파이썬에서 함수 선언은 호출보다 항상 위에 있어야 한다

from bisect import bisect_left

dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]
value = int(input('검색할 숫자 : '))

pos = bisect_left(dataset, value)
print('pos :', pos)
# 존재하지않는 수는 index에서 존재하지 않는 값이 들어가는 차례수가 나온다 
# 예) 12는 10과 18사이인 index 2가 나온다

def BinarySearch(dataset, target):
    i = bisect_left(dataset, target)
    if dataset[i] == target:
        return i
    else:
        return -1 # 값이 없습니다의 표현

value = int(input('검색할 숫자 : '))
def BinarySearch(dataset, target):

    if pos == -1:
        print('찾으실려는 숫자가 없습니다.')
    else:
        print('%d는 %d번째에 있습니다.' %(value, pos))


