"""
날짜 : 2021/09/17
이름 : 권능한
내용 : 코딩테스트 - 부품 찾기
"""

from bisect import bisect_left

# 이진탐색 라이브러리 탐색 찾기
def BinarySearch(dataset, target):

    i = bisect_left(dataset, target)

    if dataset[i] == target:

        return i
    else:
        return -1

#N(부품 갯수) 입력
n = int(input())

# 가게에 있는 전체 부품 번호를 공백 구분해서 입력
dataset = list(map(int, input().split()))
# .split 데이터를 띄워서 구분해서 받아주는 것
# 이진탐색 전 정렬은 필수 수행
# 선택정렬 처럼 어려운거 쓰지 않아도 됨.... 일반적인 정렬을 사용하자
dataset.sort()

# M(손님이 요청한 부품 갯수) 입력
m = int(input())

# 손님이 요청한 부품번호 공백 구분해서 입력
requests = list(map(int, input().split()))

# 손님이 요청한 부품번호를 하나씩 확인
for num in requests:
    # 해당 부품이 존재하는지 확인
    result = BinarySearch(dataset, num)
    if result == -1:
        print('no', end=', ')
    else:
        print('yes', end=', ')
        # ' ' -> 출력되는 문구 뒤에 공백을 넣어주기 위한 것
        # 가로로 출력하기 위한 것