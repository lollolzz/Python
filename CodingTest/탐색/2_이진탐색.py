"""
날짜 : 2021/09/17
이름 : 권능한
내용 : 코딩테스트 - 이진탐색
"""

# 이진탐색 함수
def binary_search(dataset, target):
    start = 0
    end = len(dataset) - 1
    pos = -1
    # 존재하지 않는 index값으로 초기화를 시켜주려고 하는 것

    while start <= end:
        mid = (start + end) // 2
        # / - 실수까지만 나누기 ,,,, // 정수까지만 나누기

        if dataset[mid] > target:
            end = mid - 1
        elif dataset[mid] < target:
            start = mid +1
        else:
            pos = mid
            break



    return pos

dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]
value = int(input('검색할 숫자 : '))

pos = binary_search(dataset, value)

if pos == -1:
    print('찾으실려는 숫자가 없습니다.')
else:
    print('%d는 %d번째에 있습니다.' % (value, pos))