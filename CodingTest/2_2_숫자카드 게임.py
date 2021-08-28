"""
날짜 : 21/08/13
이름 : 권능한
내용 : 코딩 테스트 - 숫자 카드 게임

"""

# n, m을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0 # 결과값

# 한 줄씩 입력 받아 확인하기
# i는 행의 숫자 3만큼만 반복
for i in range(n):
    data = list(map(int, input().split()))

    # 현재 줄에서 '가장 작은 수' 찾기
    # min()함수를 통해 해당 리스틑행의 최솟값을 구한다 그리고 data_min에 정의 해준다
    data_min = min(data)

    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    # 아래의 함수식을 통해 구해진 최솟값과 이전 최솟값을 비교하고, 최댓값을 구하여 result에 넣어둔다.
    # result값은 누적되어지므로 1행의 가장작은수 '1'을
    # re = max(1,1)은 re는 1,,,,,  re = max(1,2) 이런식으로 값을비교하며 방금 식이 마지막 행이라면
    #  re 값은 2가 된다 .
    result = max(result, data_min)

print(result) # 최종 답안