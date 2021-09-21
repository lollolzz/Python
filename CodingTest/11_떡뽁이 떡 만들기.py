"""
날짜 : 2021/09/17
이름 : 권능한
내용 : 코딩테스트 - 떡뽁이 떡 만들기

"""

# 떡의 갯수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int,input().split()))

# 각 떡의 개별 높이 정보 입력받기
dataset = list(map(int, input().split()))

# 이진 탐색을 위한 시작점 끝점
start = 0
end = max(dataset)

# 이진 탐색 수행
result = 0

while start <= end:

    total = 0

    mid = (start + end ) // 2
    for x in dataset:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += x - mid

    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1

    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:

        # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 저장
        result = mid
        start = mid + 1

# 절단기 높이 최댓값 출력
print(result)


