"""
날짜 : 21/08/13
이름 : 권능한
내용 : 코딩 테스트 - 숫자 카드 게임

"""

# n,m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
mins= []

for i in range(n):
    # 행 데이터 입력하기
    data = list(map(int, input().split()))
    # 데이터 오름차순 정렬
    data.sort()
    
    # 최소값 구하기
    min = data[0]
    
    # 각 행의 최소값 저장하기
    mins.append(min)

    # min에서 최대값 구하기
    result =max(mins)

print(result)

# answer = 0
# for i in range(n):
#     # 한 행을 공백을 기준으로 입력 받기
#     m_cards = list(map(int, input().split()))
#
#     # 입력받은 행에서의 최솟값을 찾기
#     min_number = min(m_cards)
#
#     # 현재까지 입력받은 행에서의 최솟값들 중 최댓값 answer에 저장하기
#     if answer < min_number:
#         answer = min_number
# print(answer)
